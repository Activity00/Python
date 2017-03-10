#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年3月9日

@author: 武明辉
'''
import sys

from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from twisted.python import log


class CmdProtocal(LineReceiver):
    delimiter='\n'
    def connectionMade(self):
        self.client_ip=self.transport.getPeer()
        log.msg('收到来自%s的链接'%self.client_ip)
        if len(self.factory.clients)>=self.factory.clients_max:
            log.msg('网络拥挤待会再来访问吧')
            self.client_ip=None
            self.transport.loseConnection()
        else:
            self.factory.clients.append(self.client_ip)
    
    def connectionLost(self, reason):
        log.msg('因为%s失去连连接'%reason)
        if self.client_ip:
            self.factory.clients.remove(self.client_ip)
    
    def lineReceived(self, line):
        log.msg('收到来自%s:%s'%(self.client_ip,line))

class MyFactory(ServerFactory):
    protocol=CmdProtocal
    def __init__(self,clients_max=10):
        self.clients_max=clients_max
        self.clients=[]

log.startLogging(sys.stdout)
reactor.listenTCP(9999,MyFactory(2))
reactor.run()
