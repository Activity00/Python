# coding: utf-8

"""
@author: 武明辉 
@time: 17-8-17 上午10:07
"""

from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver


class LoggingProtocol(LineReceiver):
    def lineReceived(self, line):
        print(line)
        self.factory.fp.write(line + '\n')


class LogfileFactory(Factory):
    protocol = LoggingProtocol

    def __init__(self, file_name='a1_2.log'):
        self.file = file_name
        self.fp = None

    def startFactory(self):
        self.fp = open(self.file, 'a')

    def stopFactory(self):
        self.fp.close()


endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(LogfileFactory())
reactor.run()
