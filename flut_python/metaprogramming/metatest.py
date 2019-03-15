print('1')


class ModelMeta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        print('meta mew')
        super_new = super().__new__(mcs, name, bases, attrs, **kwargs)
        print('meta end')
        return super_new

    def __init__(cls, name, bases, dic):
        print('meta init')


class Model(metaclass=ModelMeta):
    def __init__(self):
        print('model init')


class Field:
    def __set__(self, instance, value):
        super().__set__(instance, value)

    def __get__(self, instance, owner):
        super().__get__(instance, owner)


class CharField(Field):
    pass


class IntField(Field):
    pass


print('2')


class Person(Model):
    name = CharField()
    age = IntField()


print('3')


if __name__ == '__main__':
    pass
    p = Person()
    print(p.name)
    print(p.age)
