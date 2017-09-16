from texas.core.base.dict_utils import object_to_dict
from texas.game.twisted.response import broadcast, notify, TexasCommandResponseBroadcast,\
    TexasCommandResponseError, TexasCommandResponseSuccess, TexasCommandResponseNotice
from texas.game.game_controller import GameController
from texas.game.player2 import Player
from texas.core.base.lock.lock import require_lock
import time
from django.conf import settings
from texas.apps.accounts.models import TexasUser
from texas.apps.room.models import Room as Room_Model
from texas.core.base.file_url import get_file_url
from texas.core.base.utils import get_points_distance, check_two_ip_in_subnet

from texas.game.threads.check_room_action_thread import CheckRoomStartThread, CheckRoomDismissThread, RunRoomActionThread

from django_redis import get_redis_connection


class Room(object):
    def __init__(self, **kwargs):
        self.check_room_info = {
            "bring_stack": 0,
            "start": 0,
            "next_player": -1,
        }

        self.host_id = kwargs['player']  # 房主
        self.room_id = kwargs['id']
        self.name = kwargs['name']
        self.size = kwargs['size']

        self.big_blind = kwargs['big_blind']
        self.stack = self.big_blind * 100
        self.rebuy_multiple = kwargs['rebuy_multiple']
        self.ante = kwargs['ante']
        self.off_the_table_charge = kwargs['off_the_table_charge']
        self.duration = kwargs['duration']
        self.is_food_stamps = kwargs['is_food_stamps']
        self.is_authenticated = kwargs['is_authenticated']
        self.is_safe = kwargs['is_safe']
        self.is_straddled = kwargs['is_straddled']
        self.is_GPS = kwargs['is_GPS']
        self.is_IP = kwargs['is_IP']

        self.players = {} # 玩家id：玩家
        self.position_player_dict = {} # 位置：玩家
        self.player_position_dict = {} # 玩家id：位置
        self.game_controller = GameController(self)
        self.has_already_started = False

        self.status = 'pending'

    # 解散牌局，清空玩家
    def clear_room(self):
        self.players = {} # 玩家id：玩家
        self.position_player_dict = {} # 位置：玩家
        self.player_position_dict = {} # 玩家id：位置

    # 当到达牌局结束时间时，有一手牌还未结束。那么等到该手牌结束时，结束该牌局
    def dismiss(self):
        if self.game_controller.game_state.state not in ['init', 'over']:
            check_room_dismiss_thread = CheckRoomDismissThread(self)
            check_room_dismiss_thread.setDaemon(True)
            check_room_dismiss_thread.start()
        else:
            self.dismiss_room()

    def dismiss_room(self):
        self.status = 'processed'
        run_room_action_thread = RunRoomActionThread(self.broadcast_dismiss_room)
        run_room_action_thread.setDaemon(True)
        run_room_action_thread.start()

    def broadcast_dismiss_room(self):
        data = {'dismiss': '牌局结束'}
        response = TexasCommandResponseBroadcast('DismissRoom', self.host_id, data)
        player_list = [player for player, _ in self.players.values()]
        broadcast(player_list, response)

        self.change_room_model_status()

    def change_room_model_status(self):
        room = Room_Model.objects.filter(id=self.room_id).first()
        room.status = self.status
        room.save()

    # 房主解散牌局
    def host_dismiss_room(self, form, protocol):

        response = TexasCommandResponseSuccess('DismissRoom', protocol.player_id, form.cleaned_data['seq'], None)
        protocol.sendLine(response)

        self.dismiss()
        protocol.factory.room_dict.pop(self.room_id)
        for player_id in self.players.keys():
            protocol.factory.player_room_dict.pop(player_id)
        self.clear_room()

    def enter_room(self, form, protocol):
        player_id = form.cleaned_data['player_id']
        protocol.player_id = player_id

        if settings.ROBOT:
            protocol.factory.player_room_dict[player_id] = self.room_id
        else:
            # 检查player与room的关系映射
            if not protocol.factory.player_room_dict.get(player_id):
                self.broadcast_error(form, 'EnterRoom', '玩家无法进入房间', protocol)
                return

        # 游戏玩家实例
        player_obj = TexasUser.objects.filter(id=player_id).first()

        # 玩家GPS经纬度

        player = Player(player_id, player_obj.nickname, player_obj.coin, protocol, player_obj.image)

        if form.cleaned_data.get('lon') and form.cleaned_data.get('lat'):
            geo_location = (form.cleaned_data['lon'], form.cleaned_data['lat'])
            player.change_geo_location(geo_location)

        self.add_player_to_room(player)

        # 玩家进入房间，返回房间信息
        room_info = {'name': self.name, 'big_blind': self.big_blind, 'duration': self.duration,
                     'size': self.size, 'is_IP': self.is_IP, 'is_GPS': self.is_GPS}
        response = TexasCommandResponseSuccess('EnterRoom', player_id, form.cleaned_data['seq'], room_info)
        protocol.sendLine(response)

        # 通知房主，进入房间玩家列表
        host = self.get_player_by_id(self.host_id)
        player_infos = []
        # 列表初始按照玩家的加入顺序排列，先加入的玩家排在前，后加入的玩家排在后
        player_info_list = sorted(self.players.items(), key=lambda o: o[1][1])
        for player_id, player_info in player_info_list:
            player = player_info[0]
            player_info = {'id': player_id, 'name': player.name, 'image': get_file_url(player.image)}
            player_infos.append(player_info)
        notice = TexasCommandResponseNotice('EnterRoom', player_id, player_infos)
        notify(host, notice)

    @require_lock(lambda o, form, protocol: 'sitdown_' + str(form.cleaned_data['position']) + ':' + str(o.room_id))
    def _sit_down_with_lock(self, form, protocol):
        if not self.is_position_valid(form.cleaned_data['position']):
            msg = '%d位已被占，请选择其他座位' % form.cleaned_data['position']
            return False, msg

        # 该牌局设置了IP
        if self.is_IP:
            for position, player in self.position_player_dict.items():
                result = check_two_ip_in_subnet(protocol.addr.host, player.protocol.addr.host)
                if result:
                    msg = 'IP该桌已有距离相近的玩家加入'
                    return False, msg

        # 该牌局为设置了GPS
        if self.is_GPS:
            current_player = self.get_player_by_id(protocol.player_id)
            for position, player in self.position_player_dict.items():
                distance = get_points_distance(current_player.geo_location, player.geo_location)
                if distance <= 10:
                    msg = 'GPS该桌已有距离相近的玩家加入'
                    return False, msg

        player = self.get_player_by_id(protocol.player_id)
        data = {
            'title': '带入记分牌',
            'big_blind': self.big_blind,
            'stack': self.stack,
            'rebuy_multiple': self.rebuy_multiple,
            'service_charge': self.stack * 0.1,
            'coin': player.coin
        }

        # TODO 是否开启粮票
        if self.is_food_stamps:
            food_stamps = 0
            data['food_stamps'] = food_stamps

        self.add_player_at_position(form.cleaned_data['position'], player)

        return True, data

    def sit_down(self, form, protocol):
        can_sit, result = self._sit_down_with_lock(form, protocol)
        if can_sit:
            response = TexasCommandResponseSuccess('SitDown', protocol.player_id,
                                                   form.cleaned_data['seq'], result)
            protocol.sendLine(response)

            # 玩家需要在 60s 内完成带入并坐下，60s内成功带入的玩家会坐入相应的位置，60s内未成功带入的玩家被系统移出位置
            conn = get_redis_connection('redis')
            conn.zadd('texas-game-room-infos', int(time.time()) + 60, 'BringStack:' + str(self.room_id) + ':' + str(protocol.player_id))

        else:
            error = result
            response = TexasCommandResponseError('SitDown', '', form.cleaned_data['seq'], 2000, error, None, error)
            protocol.sendLine(response)

    # 取消加入牌局
    def cancel_join_room(self, form, protocol):
        self.join_room_fail(protocol.player_id)

        response = TexasCommandResponseSuccess('CancelJoinRoom', protocol.player_id,
                                               form.cleaned_data['seq'], None)
        protocol.sendLine(response)

    # 加入牌局
    def join_room(self, form, protocol):
        player = self.get_player_by_id(protocol.player_id)
        stack = form.cleaned_data['stack']
        # 标准局的服务费比默认为10%
        service_charge = 0.1
        if player.coin < stack*(1+service_charge):
            error = '您的余额不足，请先充值'
            response = TexasCommandResponseError('JoinRoom', protocol.player_id, form.cleaned_data['seq'], 2000, error, None, errors=error)
            notify(player, response)
            return

        player.bring_stack(stack)
        player.change_status('bring_stack')

        if self.is_authenticated and player.player_id != self.host_id:
            # 需要授权
            result = {'is_authenticated': True}
            response = TexasCommandResponseSuccess('JoinRoom', protocol.player_id, form.cleaned_data['seq'], result)
            notify(player, response)

            data = {'id': player.player_id, 'name': player.name, 'stack': stack}
            notice = TexasCommandResponseNotice('JoinRoom', protocol.player_id, data)
            host = self.get_player_by_id(self.host_id)
            notify(host, notice)

            # 房主120s内授权
            conn = get_redis_connection('redis')
            conn.zadd('texas-game-room-infos', int(time.time()) + 120, 'WaitingAuth:' + str(self.room_id) + ':' + str(protocol.player_id))

        else:
            # 不需要授权,坐下成功,金币扣除成功
            result = {'is_authenticated': False}
            response = TexasCommandResponseSuccess('JoinRoom', protocol.player_id, form.cleaned_data['seq'], result)
            notify(player, response)
            self.join_room_success(player.player_id)
            self.broadcast_position_players()

    def host_agree(self, form, protocol):
        is_agreed = form.cleaned_data['is_agreed']
        player_id = form.cleaned_data['player_id']
        player = self.get_player_by_id(player_id)

        if is_agreed:
            self.join_room_success(player_id)
        else:
            self.join_room_fail(player_id)

        # 命令返回
        response = TexasCommandResponseSuccess('HostAgree', protocol.player_id, form.cleaned_data['seq'], None)
        protocol.sendLine(response)

        # 通知等待坐下玩家
        data = {'is_agreed': is_agreed}
        response = TexasCommandResponseNotice('HostAgree', protocol.player_id, data)
        notify(player, response)

        if is_agreed:
            self.broadcast_position_players()

    # 扣金币
    def deduct_coin(self, player_id):
        player_obj = TexasUser.objects.filter(id=player_id).first()
        player = self.get_player_by_id(player_id)
        player_obj.coin -= player.stack * 1.1
        player_obj.save()

    def join_room_success(self, player_id):
        player = self.get_player_by_id(player_id)
        self.deduct_coin(player_id)
        player.change_status('ready')

    def broadcast_position_players(self):
        all_player_info = []
        for position, player in self.position_player_dict.items():
            if player.status == 'ready':
                player_info = {'position': position,
                               'player': object_to_dict(player, ['player_id', 'name', 'stack'], None)}
                all_player_info.append(player_info)
        response = TexasCommandResponseBroadcast('JoinRoom', 0, all_player_info)
        player_list = [player for player, _ in self.players.values()]
        broadcast(player_list, response)

    def join_room_fail(self, player_id):
        position = self.get_position_belong_to_player(player_id)
        self.remove_player_at_position(position=position)
        player = self.get_player_by_id(player_id)
        player.change_status('enter')

    # CheckThread 移除坐下失败的玩家
    def remove_player_join_fail(self, player_id):
        self.join_room_fail(player_id)
        run_room_action_thread = RunRoomActionThread(self.notify_player_join_fail, player_id)
        run_room_action_thread.setDaemon(True)
        run_room_action_thread.start()

    def notify_player_join_fail(self, player_id):
        player = self.get_player_by_id(player_id)
        data = {'JoinRoom': '坐下失败'}
        response = TexasCommandResponseNotice('JoinRoom', 0, data)
        notify(player, response)

    # CheckThread 检查玩家状态
    def check_player_status(self, player_id, status):
        player = self.get_player_by_id(player_id)
        return player.status == status

    def start(self, form, protocol):

        # Timer(self.duration, self.dismiss_room).start()
        # 牌局时长，解散牌局
        conn = get_redis_connection('redis')
        conn.zadd('texas-game-room-infos', int(time.time()) + self.duration * 3600, 'DismissRoom:' + str(self.room_id))

        # 至少坐下2人的时候,牌局开始,进入下盲注,发牌等流程
        if len(self.get_ready_players()) < 2:
            data = {'waiting': '等待其他玩家'}
            response = TexasCommandResponseSuccess('Start', protocol.player_id, form.cleaned_data['seq'], data)
            protocol.sendLine(response)
            check_number_of_players_thread = CheckRoomStartThread(self, form, protocol)
            check_number_of_players_thread.setDaemon(True)
            check_number_of_players_thread.start()
        else:
            self.start_room(form, protocol)

    def start_room(self, form, protocol):
        success, error = self.game_controller.start(self.ante, self.big_blind, self.is_straddled)
        self.has_already_started = success
        if not success:
            response = TexasCommandResponseError('Start', protocol.player_id, form.cleaned_data['seq'], 2000, error, None, error)
            protocol.sendLine(response)
        else:
            self.status = 'processing'
            # self.change_room_model_status()

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
            
    def add_player_to_room(self, player):
        self.player_position_dict[player.player_id] = -1
        self.players[player.player_id] = [player, int(time.time())]

    def add_player_at_position(self, position, player):
        self.position_player_dict[position] = player
        self.player_position_dict[player.player_id] = position

        player.change_status('sit')

    def remove_player_at_position(self, position):
        player = self.position_player_dict.pop(position)
        self.player_position_dict[player.player_id] = -1

    def get_number_of_position_players(self):
        return len(self.position_player_dict)

    def get_has_position_players(self):
        return self.position_player_dict

    def get_ready_players(self):
        active_player_dict = {}
        for position, player in self.position_player_dict.items():
            if player.status == 'ready':
                active_player_dict[position] = player
        return active_player_dict

    def get_player_by_id(self, player_id):
        player_info = self.players.get(player_id, None)
        if player_info:
            return player_info[0]
        return None

    def get_position_belong_to_player(self, player_id):
        return self.player_position_dict.get(player_id, None)
        
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