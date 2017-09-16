from twisted.internet.protocol import Factory

from texas.game.room import Room
from texas.game.twisted.robot_protocol import TexasProtocol


class TexasFactory(Factory):
    room_dict = {}
    player_room_dict = {}
    
    def buildProtocol(self, addr):
        return TexasProtocol(self)
