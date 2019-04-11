import abc


class Sourceable(abc.ABC):
    @abc.abstractmethod
    def method(self):
        pass


class SourceSub1(Sourceable):
    def method(self):
        print('sub1')


class SourceSub2(Sourceable):
    def method(self):
        print('sub2')


class Bridge:
    def __init__(self, source=None):
        self.source = source

    def method(self):
        self.source.method()

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source


class MyBridge(Bridge):
    def method(self):
        self.get_source().method()


if __name__ == '__main__':
    bridge = MyBridge()
    bridge.set_source(SourceSub1())
    bridge.method()
