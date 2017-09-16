from texas.core.base.dict_utils import object_to_dict
from texas.core.base.lock.lock import require_lock
from texas.game.game_round import GameHand, GameEvent
from texas.game.game_state import GameState
from texas.game.twisted.response import broadcast, TexasCommandResponseBroadcast, \
    TexasCommandResponseNotice, notify, TexasCommandResponseSuccess
import redis
import time

r = redis.Redis()


class GameController(object):
    def __init__(self, room):
        self.game_state = GameState(room.size)
        self.game_hand = GameHand()
        self.room = room
    
    @require_lock(lambda o, ante, big_blind, is_straddled: 'game_action_lock:' + str(o.room.room_id))
    def _start_with_lock(self, ante, big_blind, is_straddled):
        self.game_state.reset_state()
        success, error = self.game_state.start(self.room.get_ready_players(), ante=ante, limit=big_blind, is_straddled=is_straddled)
        if success:
            for active_player in self.game_state.active_players:
                self.room.get_player_at_position(active_player.position).stack = active_player.stack                
                
        return success, error

    def start(self, ante, big_blind, is_straddled):
        success, error = self._start_with_lock(ante, big_blind, is_straddled)
        if success:
            data = object_to_dict(self.game_state, ['state', 'limit', 'dealer_position', \
                'small_blind_position', 'big_blind_position', 'round_bet', 'round_all_in', \
                'current_position'])
            self.game_hand.add_event(GameEvent('start', data))
            response = TexasCommandResponseBroadcast('Start', 0, data)
            broadcast(self.room.get_has_position_players().values(), response)
            
            for player in self.game_state.active_players:
                response = TexasCommandResponseNotice('HoleCards', 0, { 'hole_cards': player.hole_cards })
                notify(self.room.get_player_at_position(player.position), response)

            self.build_new_round_and_notify_next_player()

            return True, self.game_state
        else:
            return False, error

    @require_lock(lambda o, _: 'game_action_lock:' + str(o.room.room_id))
    def _call_with_lock(self, position):
        success, error = self.game_state.call(position)
        if success:
            player_state = self.game_state.active_players[self.game_state.active_player_positions.index(position)]
            self.room.get_player_at_position(position).stack = player_state.stack
        return success,  error

    def call(self, form, protocol):
        if protocol.player_id == -1:
            return False, '玩家不存在'
        position = self.room.player_position_dict[protocol.player_id]
        success, error = self._call_with_lock(position)
        if success:
            self.notify_commander_result('Call', position, form)
            self.broadcast_command_result('Call', position)

            self.build_new_round_and_notify_next_player()

            return True, self.game_state
        else:
            return False, error

    @require_lock(lambda o, position, chips: 'game_action_lock:' + str(o.room.room_id))
    def _bet_with_lock(self, position, chips):
        success, error = self.game_state.bet(position, chips)
        if success:
            player_state = self.game_state.active_players[self.game_state.active_player_positions.index(position)]
            self.room.get_player_at_position(position).stack = player_state.stack
        return success, error

    def bet(self, form, protocol):
        if protocol.player_id == -1:
            return False, '玩家不存在'
        position = self.room.player_position_dict[protocol.player_id]
        chips = form.cleaned_data['chips']
        success, error = self._bet_with_lock(position, chips)
        if success:
            self.notify_commander_result('Bet', position, form)
            self.broadcast_command_result('Bet', position)
            self.notify_next_player()
            return True, self.game_state
        else:
            return False, error

    @require_lock(lambda o, _: 'game_action_lock:' + str(o.room.room_id))
    def _all_in_with_lock(self, position):
        success, error = self.game_state.all_in(position)
        if success:
            player_state = self.game_state.active_players[self.game_state.active_player_positions.index(position)]
            self.room.get_player_at_position(position).stack = player_state.stack
        return success,  error

    def all_in(self, form, protocol):
        if protocol.player_id == -1:
            return False, '玩家不存在'
        position = self.room.player_position_dict[protocol.player_id]
        success, error = self._all_in_with_lock(position)
        if success:
            self.notify_commander_result('AllIn', position, form)
            self.broadcast_command_result('AllIn', position)

            self.build_new_round_and_notify_next_player()

            return True, self.game_state
        else:
            return False, error

    @require_lock(lambda o, _: 'game_action_lock:' + str(o.room.room_id))
    def _check_with_lock(self, position):
        success, error = self.game_state.check(position)
        return success,  error

    def check(self, form, protocol):
        if protocol.player_id == -1:
            return False, '玩家不存在'
        position = self.room.player_position_dict[protocol.player_id]
        success, error = self._check_with_lock(position)
        if success:
            self.notify_commander_result('Check', position, form)
            self.broadcast_command_result('Check', position)

            self.build_new_round_and_notify_next_player()

            return True, self.game_state
        return False, error

    @require_lock(lambda o, position, chips: 'game_action_lock:' + str(o.room.room_id))
    def _raise_with_lock(self, position, chips):
        success, error = self.game_state.raise_chips(position, chips)
        if success:
            player_state = self.game_state.active_players[self.game_state.active_player_positions.index(position)]
            self.room.get_player_at_position(position).stack = player_state.stack
        return success,  error

    def raise_chips(self, form, protocol):
        if protocol.player_id == -1:
            return False, '玩家不存在'
        position = self.room.player_position_dict[protocol.player_id]
        chips = form.cleaned_data['chips']
        success, error = self._raise_with_lock(position, chips)
        if success:
            self.notify_commander_result('Raise', position, form)
            self.broadcast_command_result('Raise', position)
            self.notify_next_player()
            return True, self.game_state
        return False, error

    @require_lock(lambda o, _: 'game_action_lock:' + str(o.room.room_id))
    def _fold_with_lock(self, position):
        success, error = self.game_state.fold(position)
        return success,  error

    def fold(self, form, protocol):
        if protocol.player_id == -1:
            return False, '玩家不存在'
        position = self.room.player_position_dict[protocol.player_id]
        result, error = self._fold_with_lock(position)
        if result:
            self.notify_commander_result('Fold', position, form)
            self.broadcast_command_result('Fold', position)
            if not self.game_state.check_only_one_player():
                self.build_new_round_and_notify_next_player()
            # TODO Current hand is over.
            else:
                self.broadcast_game_over()

            return True, self.game_state
        return False, error

    def check_can_new_round(self):
        self.game_state.check_can_build_new_round()
        if self.game_state.is_new_round:
            self.broadcast_new_round()

    def build_new_round_and_notify_next_player(self):
        while self.game_state.state != 'over':
            self.check_can_new_round()
            if self.game_state.current_position != None:
                self.notify_next_player()
                break
        if self.game_state.state == 'over':
            self.broadcast_game_over()

    def broadcast_new_round(self):
        cards = None
        if self.game_state.state == 'flop':
            cards = self.game_state.flop_cards
        elif self.game_state.state == 'turn':
            cards = self.game_state.turn_card
        elif self.game_state.state == 'river':
            cards = self.game_state.river_card

        if self.game_state.side_pot:
            if self.game_state.side_pot[-1][0] == 0:
                self.game_state.side_pot.pop()

        side_pot = [{'pot': pot[0], 'positions': pot[1]} for _, pot in enumerate(self.game_state.side_pot)]

        data = {
            'state': self.game_state.state,
            'next_position': self.game_state.current_position,
            'cards': cards,
            'pot': self.game_state.pot,
            'side_pot': side_pot
        }

        self.game_hand.add_event(GameEvent(self.game_state.state, data))
        response = TexasCommandResponseBroadcast(self.game_state.state.capitalize(), 0, data)
        broadcast(self.room.get_has_position_players().values(), response)

    def broadcast_command_result(self, command, position):
        data = object_to_dict(self.game_state, ['state', 'round_bet', 'round_all_in'])
        data['next_position'] = self.game_state.current_position
        self.game_hand.add_event(GameEvent(command, data))
        response = TexasCommandResponseBroadcast(command, self.room.get_player_at_position(position).player_id, data)
        broadcast(self.room.get_has_position_players().values(), response)

    def notify_commander_result(self, command, position, form):

        index = self.game_state.active_player_positions.index(position)
        player_state = self.game_state.active_players[index]
        player = self.room.position_player_dict[position]
        data = {
            'stack': player_state.stack,
            'state': player_state.state
        }
        self.game_hand.add_event(GameEvent(command, data))
        response = TexasCommandResponseSuccess(command, player_state.player_id, form.cleaned_data['seq'], data)
        notify(player, response)

    def notify_next_player(self):
        available_actions = self.game_state.get_available_actions()
        data = {'available_actions': self.game_state.get_available_actions()}
        if 'raise' in available_actions:
            to_raise = self.game_state.get_to_raise() - self.game_state.round_bet.get(self.game_state.current_position, 0)
            data['to_raise'] = to_raise
        response = TexasCommandResponseNotice('InTurn', 0, data)
        notify(self.room.get_player_at_position(self.game_state.current_position), response)

        # #TODO  After 30s, auto fold!
        # self.room.check_version['next_player'] = self.room.get_player_at_position(self.game_state.current_position).player_id
        # r.zadd('fold:' + str(self.room.room_id), self.room.check_version['next_player'], int(time.time()) + 30)

    def broadcast_game_over(self):
        player_hand_list = []
        winner_hand_list = []
        for player in self.game_state.final_players:
            player_info = object_to_dict(player, ['player_id', 'position', 'hand', 'hole_cards'])
            player_hand_list.append(player_info)
            for player_win_pot in self.game_state.win_players:
                if player == player_win_pot[0]:
                    self.room.get_player_at_position(player.position).stack = player.stack
                    winner_player_info = player_info.copy()
                    winner_player_info['stack'] = player.stack
                    winner_player_info['win_pot'] = player_win_pot[1]
                    winner_hand_list.append(winner_player_info)

        data = {
            'player_hand_list': player_hand_list,
            'winners': winner_hand_list
        }
        self.game_hand.add_event(GameEvent(self.game_state.state, data))
        response = TexasCommandResponseBroadcast(self.game_state.state, 0, data)
        broadcast(self.room.get_has_position_players().values(), response)


