# coding: utf-8

"""
@author: 武明辉 
@time: 2018/7/1 17:56
"""
from utils import time_this

"""
反转整数不使用第三方库
"""


@time_this()
def reverse_int0(num):
    num_list = list(str(num))
    num_list.reverse()
    return ''.join(num_list)


@time_this()
def reverse_int(num):
    tmp = []
    while num // 10 > 0:
        tmp.insert(0, num % 10)
        num //= 10
    tmp.insert(0, num % 10)

    ret = 0
    for i, v in enumerate(tmp):
        ret += v * (10 ** i)
    return ret

if __name__ == '__main__':
    """
    总用时: 0.000024 s
    58924
    总用时: 0.000009 s
    58924
    """
    print(reverse_int(42985))
    print(reverse_int0(42985))
