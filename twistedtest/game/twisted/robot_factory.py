from twisted.internet.protocol import Factory

from texas.game.twisted.robot_protocol import TexasProtocol


class TexasFactory(Factory):
    def buildProtocol(self, addr):
        return TexasProtocol(self)
