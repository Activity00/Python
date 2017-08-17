# coding:utf-8
# !usr/bin/env python
"""
Created on 2017年3月6日

@author: 武明辉
"""
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint


class Echo(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write("Welcome! There are currently %d open connections.\n" %(self.factory.numProtocols,))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        self.transport.write(data)


class QOTD(Protocol):
    def connectionMade(self):
        self.transport.write(bytes('hello\n', encoding='utf-8'))
        self.transport.loseConnection()


class QOTDFactory(Factory):
    def buildProtocol(self, addr):
        print(addr)
        return QOTD()


endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory())
reactor.run()


