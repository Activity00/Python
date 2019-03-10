# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-10 上午10:53
"""


class A:
    a = 'aaa'

    def __init__(self):
        print('inti')

    def __new__(cls, *args, **kwargs):
        print('new')
        return super().__new__(cls)


if __name__ == '__main__':
    a = A()
    print(vars(a))
    print(a.__dict__)
    a.a = 2
    print(vars(a))
    print(a.__dict__)
    print(dir(a))
