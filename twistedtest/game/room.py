from texas.core.base.dict_utils import object_to_dict
from texas.game.twisted.response import broadcast, notify, TexasCommandResponseBroadcast, TexasCommandResponseError, TexasCommandResponseSuccess
from texas.game.game_controller import GameController
from texas.game.player import Player
from texas.core.base.lock.lock import require_lock
import redis
import time

r = redis.Redis()


class Room(object):
    def __init__(self, name, size, room_id):
        self.check_version = {
            "start": 0,
            "next_player": -1,
        }

        self.name = name
        self.size = size
        self.room_id = room_id
        self.players = {}
        self.position_player_dict = {} # 位置：玩家
        self.player_position_dict = {} # 玩家id：位置
        self.game_controller = GameController(self)
        self.has_already_started = False
        
    def enter_room(self, form, protocol):
        player_id = form.cleaned_data['player_id']
        self.add_player_to_room(player_id)
        protocol.player_id = player_id

        # 增加player与room的关系映射
        protocol.factory.player_room_dict[player_id] = form.cleaned_data['room_id']

        response = TexasCommandResponseSuccess('EnterRoom', player_id, form.cleaned_data['seq'], None)
        protocol.sendLine(response)

    @require_lock(lambda o, form, protocol: 'sitdown_' + str(form.cleaned_data['position']) + ':' + str(o.room_id))
    def _sit_down_with_lock(self, form, protocol):
        if protocol.player_id == -1:
            return False, "玩家不存在"
        if self.is_position_valid(form.cleaned_data['position']):
            player = Player(protocol.player_id, form.cleaned_data['name'],
                            form.cleaned_data['chips'], protocol)
            self.add_player_at_position(form.cleaned_data['position'], player)
            return True, player
        return False, '%d位已被占，请选择其他座位' % form.cleaned_data['position']

    def sit_down(self, form, protocol):

        self.check_version['start'] += 1
        r.zadd('start:' + str(self.room_id), self.check_version['start'], int(time.time()) + 5)

        can_sit, result = self._sit_down_with_lock(form, protocol)
        if can_sit:
            player = result
            response = TexasCommandResponseSuccess('SitDown', player.player_id, form.cleaned_data['seq'], None)
            notify(player, response)
            all_player_info = []
            for position, player in self.position_player_dict.items():
                player_info = {'position': position, 'player': object_to_dict(player, ['player_id', 'name', 'stack'], None)}
                all_player_info.append(player_info)
            response = TexasCommandResponseBroadcast('SitDown', player.player_id, all_player_info)
            broadcast(self.position_player_dict.values(), response)
        else:
            error = result
            response = TexasCommandResponseError('SitDown', '', form.cleaned_data['seq'], 2000, error, None, error)
            protocol.sendLine(response)

    def start(self):
        success, error = self.game_controller.start()
        self.has_already_started = success
        if not success:
            #TODO form and protocol
            print('Error')
            # response = TexasCommandResponseError('Start', '', form.cleaned_data['seq'], 2000, error, None, error)
            # protocol.sendLine(response)

    def has_started(self):
        return self.has_already_started

    def get_room_state(self, form, protocol):
        game_state = self.game_controller.game_state
        data = object_to_dict(game_state, ['state', 'limit', 'dealer_position',
                                                'small_blind_position', 'big_blind_position', 'round_bet',
                                                'round_all_in',
                                                'current_position'])

        response = TexasCommandResponseBroadcast('GetRoomState', '', data)
        broadcast(self.position_player_dict.values(), response)

    def bet(self, form, protocol):
        success, error = self.game_controller.bet(form, protocol)
        if not success:
            self.broadcast_error(form, 'Bet', error, protocol)

    def call(self, form, protocol):
        success, error = self.game_controller.call(form, protocol)
        if not success:
            self.broadcast_error(form, 'Call', error, protocol)

    def all_in(self, form, protocol):
        success, error = self.game_controller.all_in(form, protocol)
        if not success:
            self.broadcast_error(form, 'Call', error, protocol)

    def check(self, form, protocol):
        success, error = self.game_controller.check(form, protocol)
        if not success:
            self.broadcast_error(form, 'Check', error, protocol)

    def raise_chips(self, form, protocol):
        success, error = self.game_controller.raise_chips(form, protocol)
        if not success:
            self.broadcast_error(form, 'Raise', error, protocol)

    def fold(self, form, protocol):
        success, error = self.game_controller.fold(form, protocol)
        if not success:
            self.broadcast_error(form, 'Fold', error, protocol)
            
    def add_player_to_room(self, player_id):
        self.player_position_dict[player_id] = -1

    def add_player_at_position(self, position, player):
        self.position_player_dict[position] = player
        self.player_position_dict[player.player_id] = position

        #TODO players map
        self.players[player.player_id] = player

    def remove_player_at_position(self, position):
        player = self.position_player_dict.pop(position)
        self.player_position_dict[player.player_id] = -1
        
    def get_has_position_players(self):
        return self.position_player_dict

    def get_player_by_id(self, player_id):
        return self.players.get(player_id, None)
        
    def get_player_at_position(self, position):
        return self.position_player_dict.get(position, None)

    def is_position_valid(self, position):
        if position in self.position_player_dict.keys():
            return False
        return True

    def broadcast_error(self, form, command, error, protocol):
        response = TexasCommandResponseError(command, protocol.player_id, form.cleaned_data['seq'], 2000, error, None, error)
        protocol.sendLine(response)

    def debug(self, form, protocol):
        position_player_dict = {}
        for position, player in self.position_player_dict.items():
            player_data_dict = object_to_dict(player, ['player_id', 'name', 'stack'])
            position_player_dict[position] = player_data_dict

        room_data = object_to_dict(self, ['player_position_dict'])
        game_state = self.game_controller.game_state
        game_state_data = object_to_dict(game_state, ['state', 'limit', 'to_call', 'to_raise', 'pot',
                                                      'side_pot', 'round_bet', 'open', 'round_all_in',
                                                      'max_position_count', 'active_player_count', 'active_player_positions',
                                                      'fold_player_positions', 'dealer_position',
                                                      'small_blind_position', 'big_blind_position', 'current_position',
                                                      'is_new_round', 'flop_cards', 'turn_card', 'river_card'])

        active_players = game_state.active_players
        active_player_list = []
        for active_player in active_players:
            active_player_dict = object_to_dict(active_player, ['state', 'player_id', 'position', 'stack', 'hole_cards'])
            active_player_list.append(active_player_dict)
        game_state_data['active_players'] = active_player_list
        room_data['position_player_dict'] = position_player_dict
        room_data['game_state'] = game_state_data
        response = TexasCommandResponseBroadcast('GetRoomState', '', room_data)
        broadcast(self.position_player_dict.values(), response)