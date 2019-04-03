from abc import ABC
import abc


class Person(ABC):

    @abc.abstractmethod
    def build_head(self):
        pass

    @abc.abstractmethod
    def build_body(self):
        pass

    @abc.abstractmethod
    def build_footer(self):
        pass


class Thin(Person):
    def build_head(self):
        print('小头')

    def build_body(self):
        print('小身体')

    def build_footer(self):
        print('小footer')


class Fat(Person):
    def build_head(self):
        print('大头')

    def build_body(self):
        print('大身体')

    def build_footer(self):
        print('大footer')


class Direction:
    def __init__(self, person):
        self.person = person

    def build(self):
        self.person.build_head()
        self.person.build_body()
        self.person.build_footer()


if __name__ == '__main__':
    fater = Fat()
    tiner = Thin()
    f = Direction(fater)
    f.build()
    t = Direction(tiner)
    t.build()
