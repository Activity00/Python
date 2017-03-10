#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年3月9日

@author: 武明辉
'''
from twisted.internet import defer, reactor


class Getter(object):
    def getData(self,x):
        d=defer.Deferred()
        reactor.callLater(2,d.callback,x*3)
        return d
def printd(d):
    print d

g=Getter()
d=g.getData(3)
d.addCallback(printd)

reactor.callLater(4,reactor.stop)
reactor.run()

