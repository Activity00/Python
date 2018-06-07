# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/26 9:11
"""
import doctest
from functools import lru_cache


@lru_cache()
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n-2) + fib(n-1)


def fib_p(n):
    a = b = 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return a


def fib_pp(n):
    m, a, b = 0, 0, 1
    while m < n:
        yield b
        a, b = b, a+b
        m += 1


if __name__ == '__main__':
    doctest.testmod()
