# coding: utf-8

"""
@author: 武明辉 
@time: 17-9-26 上午10:14
"""


class Base(object):
    def __init__(self):
        print('in base')
        print('out base')


class A(Base):
    def __init__(self):
        print('in A')
        super(A, self).__init__()
        print('out A')


class B(Base):
    def __init__(self):
        print('in B')
        super(B, self).__init__()
        print('out B')


class C(A, B):
    def __init__(self):
        print('in C')
        super(C, self).__init__()
        print('out C')


if __name__ == '__main__':
    c = C()
    print(C.mro())
