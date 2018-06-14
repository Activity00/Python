# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/14 11:02
"""
from twisted.internet import reactor, defer
from twisted.web.client import getPage


def response(content):
    print(content)


@defer.inlineCallbacks
def task():
    url = 'http://www.baidu.com'
    d = getPage(url.encode())
    d.addCallback(response)
    yield d
    url = 'http://www.baidu.com'
    d = getPage(url.encode())
    d.addCallback(response)
    yield d


def done(*args, **kwargs):
    reactor.stop()


if __name__ == '__main__':
    li = [task() for _ in range(10)]
    dd = defer.DeferredList(li)
    dd.addBoth(done)
    reactor.run()
