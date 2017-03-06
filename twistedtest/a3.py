#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年3月6日

@author: 武明辉
'''
from sys import stdout

from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol


class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)

class WelcomeMessage(Protocol):
    def connectionMade(self):
        self.transport.write("Hello server, I am the client!\r\n")
        self.transport.loseConnection()     
        
class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("MESSAGE%s\n" % msg)

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sendMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)    

point = TCP4ClientEndpoint(reactor, "localhost", 1234)
d = connectProtocol(point, Greeter())
d.addCallback(gotProtocol)
reactor.run()
creator = ClientCreator(reactor, Greeter)
d = creator.connectTCP("localhost", 1234)
d.addCallback(gotProtocol)
reactor.run()