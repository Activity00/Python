# coding: utf-8

"""
@author: 武明辉 
@time: 17-8-17 下午2:11
"""
from twisted.internet import reactor, protocol, defer


class CallbackAndDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.deferred.callback('Connected!')
        self.transport.loseConnection()


class ConnectioonTestFactory(protocol.ClientFactory):
    protocol = CallbackAndDisconnectProtocol

    def __init__(self):
        self.deferred = defer.Deferred()

    def clientConnectionFailed(self, connector, reason):
        self.deferred.errback(reason)


def testConnect(host, port):
    testFactory = ConnectioonTestFactory()
    reactor.connectTCP(host, port, testFactory)
    return testFactory.deferred


def handleSuccess(port):
    print('connect to {}'.format(port))
    reactor.stop()


def handleFailure(failure,port):
    print('can not connect to {} :{}'.format(port,failure.getErrorMessage()))
    reactor.stop()


if __name__ == '__main__':
    import sys
    if not len(sys.argv) == 3:
        print('Usage:coonnections host port')
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    connecting = testConnect(host, port)
    connecting.addCallback(handleSuccess, port)
    connecting.addErrback(handleFailure, port)
    reactor.run()
