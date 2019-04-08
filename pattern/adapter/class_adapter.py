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


class Adapter(Source, Target):
    def special_request(self):
        print('special request')


if __name__ == '__main__':
    adapter = Adapter()
    adapter.request()
    adapter.special_request()
