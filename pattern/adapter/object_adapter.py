import abc


class Source:
    def request(self):
        print('normal request')


class Target(abc.ABC):
    @abc.abstractmethod
    def request(self):
        pass

    @abc.abstractmethod
    def special_request(self):
        pass


class Wrapper(Target):
    def __init__(self, source):
        self.source = source

    def request(self):
        self.source.request()

    def special_request(self):
        print('special request')


if __name__ == '__main__':
    adapter = Wrapper(Source())
    adapter.request()
    adapter.special_request()
