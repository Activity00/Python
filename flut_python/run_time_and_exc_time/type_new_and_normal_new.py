class ModelMeta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        print('meta mew')
        super_new = super().__new__(mcs, name, bases, attrs, **kwargs)
        print('meta end')
        return super_new

    def __init__(cls, name, bases, dic):
        print('meta init')


class TypeChild(metaclass=ModelMeta):
    pass


class Normalnew:
    def __new__(cls, *args, **kwargs):
        print('normal new')
        super_new = super().__new__(cls, *args, **kwargs)
        print('normal end')
        return super_new

    def __init__(self):
        print('normal init')


if __name__ == '__main__':
    Normalnew()
