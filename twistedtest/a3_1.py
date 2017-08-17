# coding: utf-8

"""
@author: 武明辉 
@time: 17-8-17 上午11:12
"""
from sys import stdout

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory


class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)


class EchoClientFactory(ClientFactory):

    def startedConnecting(self, connector):
        print('start to connect')

    def buildProtocol(self, addr):
        print('connteted')
        return Echo

    def clientConnectionLost(self, connector, reason):
        print('Lost connection Reason:', reason)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print('connection failed. Reason:', reason)

reactor.connectTCP('host', 8123, EchoClientFactory())
reactor.run()