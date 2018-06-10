# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/10 10:49
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    ret = int(str(abs(x))[::-1])
    return ret * ((x > 0) - (x < 0)) if -2 ** 31 <= ret <= 2 ** 31 - 1 else 0

if __name__ == '__main__':
    pass
