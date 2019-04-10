import abc


class Sourceable(abc.ABC):

    @abc.abstractmethod
    def method(self):
        pass


class Source(Sourceable):
    def method(self, *args, **kwargs):
        print('normal source')


class SourceProxy(Sourceable):

    def __init__(self):
        self.source = Source()

    def method(self, *args, **kwargs):
        print('before')
        self.source.method(*args, **kwargs)
        print('after')


if __name__ == '__main__':
    s = Source()
    d = SourceProxy()
    d.method()
