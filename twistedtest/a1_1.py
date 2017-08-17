# coding: utf-8

"""
@author: 武明辉 
@time: 17-8-17 上午9:58
"""
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Protocol, Factory


class QOTD(Protocol):
    def connectionMade(self):
        self.transport.write(bytes(self.factory.quote + '\r\n', encoding='utf-8'))
        self.transport.loseConnection()


class QOTDFactory(Factory):
    protocol = QOTD

    def __init__(self, quote=None):
        self.quote = quote or 'An App a day keeps the doctor away'


endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory())
reactor.run()
