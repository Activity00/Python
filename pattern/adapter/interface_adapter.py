import abc


class Target(abc.ABC):
    @abc.abstractmethod
    def request(self):
        pass

    @abc.abstractmethod
    def special_request(self):
        pass


class Wrapper(Target):
    def request(self):
        pass

    def special_request(self):
        pass


class TargetSub1(Wrapper):
    def request(self):
        print('normal request')


class TargetSub2(Wrapper):
    def special_request(self):
        print('special request')


if __name__ == '__main__':
    t1 = TargetSub1()
    t2 = TargetSub2()
    t1.request()
    t2.special_request()
