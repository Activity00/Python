# coding: utf-8

"""
@author: 武明辉 
@time: 17-8-17 上午11:28
"""
from sys import stdout

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ReconnectingClientFactory


class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)


class EchoClientFactory(ReconnectingClientFactory):

    def startedConnecting(self, connector):
        print('start to connect')

    def buildProtocol(self, addr):
        print('connteted')
        print('resetting reconnection delay')
        self.resetDelay()
        return Echo

    def clientConnectionLost(self, connector, reason):
        print('Lost connection Reason:', reason)
        ReconnectingClientFactory.clientConnectionLost(self,connector,reason)

    def clientConnectionFailed(self, connector, reason):
        print('connection failed. Reason:', reason)
        ReconnectingClientFactory.clientConnectionFailed(self,connector,reason)

reactor.connectTCP('host', 8123, EchoClientFactory())
reactor.run()
