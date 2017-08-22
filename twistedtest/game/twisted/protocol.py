from twisted.protocols.basic import LineOnlyReceiver

from texas.game.commands.command_parser import CommandParser
from texas.game.twisted.response import TexasCommandResponseError


class TexasProtocol(LineOnlyReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.player_id = -1

    def sendLine(self, line):
        line = str(line)
        # print(line)
        line_bytes = line.encode(encoding='utf_8', errors='strict')
        return super(TexasProtocol, self).sendLine(line_bytes)
    
    def lineReceived(self, line):
        # print(line)
        command, status, message = CommandParser.parse(self.factory, self, line)
        if not command:
            if status == 400:
                response = TexasCommandResponseError('', '', '', 400, '请求参数错误', errors=message)
            else:
                response = TexasCommandResponseError('', '', '', status, message)
            self.sendLine(response)
        else:
            command.run()
