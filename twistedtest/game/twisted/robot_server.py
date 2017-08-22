from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint


def main():
    from texas.game.twisted.robot_factory import TexasFactory
    factory = TexasFactory()
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(factory)
    reactor.run()


if __name__ == "__main__":
    main()

