"""
java format
"""

import abc


class Sourceable(abc.ABC):

    @abc.abstractmethod
    def method(self):
        pass


class Source(Sourceable):
    def method(self):
        print('normal source')


class Decorator(Sourceable):

    def __init__(self, source):
        self.source = source

    def method(self, *args, **kwargs):
        print('before')
        self.source.method(*args, **kwargs)
        print('after')


if __name__ == '__main__':
    s = Source()
    d = Decorator(s)
    d.method()
