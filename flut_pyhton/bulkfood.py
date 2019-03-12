
# *************************version1***************************************


class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        """
        必须用__dict__否则会会循环引用
        """
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('Value must be > 0')


class LinItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

# *************************version2***************************************


class Quantity1:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        """
        必须用__dict__否则会会循环引用
        """
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('Value must be > 0')


class LinItem1:
    weight = Quantity1()
    price = Quantity1()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def test():
    LinItem('xxx', 10, 0)


def test1():
    counters = LinItem1('xxx', 10, 20)
    print(counters.price)
    print(counters.weight)


if __name__ == '__main__':
    test1()
