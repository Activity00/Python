import os

from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "texas.settings")
    import django
    django.setup()
    from texas.game.twisted.robot_factory import TexasFactory
    factory = TexasFactory()
    endpoint = TCP4ServerEndpoint(reactor, 16014)
    endpoint.listen(factory)
    reactor.run()


if __name__ == '__main__':
    main()


