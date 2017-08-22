from twisted.internet.protocol import Factory

from texas.game.room import Room
from texas.game.twisted.protocol import TexasProtocol


class TexasFactory(Factory):
    room_dict = {1: Room('test', 6, 1)}
    player_room_dict = {}

    def buildProtocol(self, addr):
        return TexasProtocol(self)
