# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/15 9:58
"""
from twisted.internet import reactor, defer


def task():
    print('xxx')
    d = defer.Deferred()
    d.addCallback(None)
    return d

if __name__ == '__main__':
    d = task()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
