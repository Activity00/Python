import json
import os
import time
import types

from twisted.protocols.basic import LineOnlyReceiver

from texas.game import commands
from texas.game.room import Room


def deal(self):
    self.deck.cards = self.cards_temp
    self.dealer_position = self.position_temp
    hole_card_list = self.deck.deal(len(self.active_player_positions))
    for i in range(self.active_player_count):
        self.active_players[(self.active_player_positions.index(
            self.dealer_position) + i + 1) % self.active_player_count].hole_cards = \
            hole_card_list[i]


class RobotProtocol:
    def __init__(self, factory, name):
        self.factory = factory
        self.name = name
    
    def sendLine(self, line):
        print('{}:{}'.format(self.name, line))


class TexasProtocol(LineOnlyReceiver):
    SLEEP_TIME = 1

    def __init__(self, factory):
        self.factory = factory
        self.lines, self.lines_length = None, 0
        self.index = 0
        self.robots = {}  # name: RobotProtocol
        self.room_id = 0

    def lineReceived(self, line):
        if isinstance(line, bytes):
            line = str(line, encoding='utf8')
        try:
            data = json.loads(line)
        except:
            self.sendLine('{"seq": "seq", "status": 404, "message": "发送的不是json", "type": "command_result"}')
            return

        result = self.__chek_client_para(data)
        if not result:
            self.sendLine('{"seq": "seq", "status": 404, "message": "与脚本不一致", "type": "command_result"}')
            return

        Command = getattr(commands, data['command'] + 'Command', None)
        command = Command(self.factory, self, data)
        command.is_valid()
        command.run()

        if data['command'] != 'EnterRoom':
            self.index += 1
        if self.index >= self.lines_length:
            return
        time.sleep(TexasProtocol.SLEEP_TIME)

        self.robot_loop()

    def robot_loop(self):
        while not self.lines[self.index].startswith('P'):
            if self.lines[self.index].startswith('#') or self.lines[self.index].strip() == '':
                self.index += 1
                if self.index >= self.lines_length:
                    return
                continue

            if self.lines[self.index].startswith('C'):
                self.__cards_command(self.lines[self.index])
                self.index += 1
                if self.index >= self.lines_length:
                    return
                continue

            if self.lines[self.index].startswith('D'):
                self.__dealer_position_command(self.lines[self.index])
                self.index += 1
                if self.index >= self.lines_length:
                    return
                continue

            if self.lines[self.index].startswith('S'):
                self.__start_command(self.lines[self.index])
                self.index += 1
                if self.index >= self.lines_length:
                    return
                continue

            self.execute_cmd(self.lines[self.index])
            self.index += 1
            if self.index >= self.lines_length:
                return
            time.sleep(TexasProtocol.SLEEP_TIME)

    def sendLine(self, line):
        line = str(line)
        line_bytes = line.encode(encoding='utf_8', errors='strict')
        return super(TexasProtocol, self).sendLine(line_bytes)

    def execute_cmd(self, line):
        command = self.parse_cmd(line)
        command.is_valid()
        data = command.data
        command.run()

    def parse_cmd(self, line):
        data = self.parse_rbt(line)
        Command = getattr(commands, data['command'] + 'Command')
        name = data['name']
        if name.startswith('C'):
            protocol = self
        else:
            protocol = self.robots.get(name, None)
            if not protocol:
                protocol = RobotProtocol(self.factory, data['name'])
                self.robots[name] = protocol
        command = Command(self.factory, protocol, data)
        return command

    def __cards_command(self, line):
        lines = line.split()
        cards_list = lines[1].split(',')
        room = self.factory.room_dict.get(self.room_id)
        room.game_controller.game_state.cards_temp = cards_list
        room.game_controller.game_state.deal = types.MethodType(deal, room.game_controller.game_state)

    def __dealer_position_command(self, line):
        position = int(line.split()[1])
        room = self.factory.room_dict.get(self.room_id)
        room.game_controller.game_state.position_temp = position

    def __start_command(self, line):
        data = {"command": "Start", "seq": "seq"}
        Command = getattr(commands, line.split()[0] + 'Command')
        command = Command(self.factory, self, data)
        command.is_valid()
        command.run()

    def __chek_client_para(self, data):
        if data.get('command') and data.get('command') == 'EnterRoom':
            if data.get('room_id') == 0 or data.get('room_id') is not None:
                self.create_room(data['room_id'])
                self.get_file_data(data['room_id'])
                return True
            else:
                return False

        line = self.lines[self.index]
        data_o = self.parse_rbt(line)
        for k, v in data_o.items():
            if k == 'name':
                continue
            vl = data.get(k, None)
            if vl or vl == 0:
                if vl == v or vl == 'seq':
                    continue
                else:
                    pass
            else:
                return False
        return True

    @staticmethod
    def parse_rbt(line):
        lines = line.split()
        data = {'name': lines[0], 'command': lines[1], 'seq': 'seq'}
        for para in lines[2:]:
            temp = para.split(':')
            if temp[1].isdigit():
                data[temp[0]] = int(temp[1])
            else:
                data[temp[0]] = temp[1]

        return data

    def get_file_data(self, room_num):
        file_path = os.path.join(os.path.dirname(__file__), 'robot_script')
        with open(os.path.join(file_path, 'room_%s.txt' % room_num)) as fp:
            self.lines = fp.readlines()
            self.room_id = int(room_num)
        self.lines_length = len(self.lines)
        fp.close()

    def create_room(self, room_num):
        para = {'id': int(room_num), 'name': 'robot', 'size': 9, 'big_blind': 10, 'scoreboard_multiple_mix': 10,
                'scoreboard_multiple_max': 1000, 'ante': 20, 'off_table_charge': 100, 'duration': 1000,
                'is_food_stamps': False, 'is_authenticated': True, 'is_safe':True, 'is_straddled': True,
                'is_GPS': True, 'is_IP': True, 'rebuy_multiple':None,'off_the_table_charge': None}

        self.factory.room_dict = {int(room_num): Room(**para)}
