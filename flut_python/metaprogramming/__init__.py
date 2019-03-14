# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-10 上午10:53
"""


class A:
    a = 'aaa'

    def __init__(self):
        print('inti')

    def xx(self):
        pass

    def bb(self):
        pass

if __name__ == '__main__':
    a = A()
    print(A.__dict__)
