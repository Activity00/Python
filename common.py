# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/26 16:17
"""
import doctest

"""
最小公约数最大公倍数
-- 辗转相除法
1. a % b -> c
2. if c == 0 b is answer
"""


def max_common_o(a, b):
    """
    >>> max_common_o(36, 21)
    3
    """
    sm = b if a > b else a
    while sm:
        if a % sm == 0 and b % sm == 0:
            return sm
        sm -= 1
    return 1


def max_common(a, b):
    """
    >>> max_common(36, 21)
    3
    """
    while b:
        a, b = b, a%b
    return a


def min_common(a, b):
    c = a * b
    x = max_common(a, b)
    return c // x

if __name__ == '__main__':
    doctest.testmod()
