# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-10 下午2:53
"""


def quatity(name):
    def qty_getter(instance):
        return instance.__dict__[name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quatity('weight')
    price = quatity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    print(nutmeg.weight, nutmeg.price)
    print(sorted(vars(nutmeg).items()))
    nutmeg.price = -1
