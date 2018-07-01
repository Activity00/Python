# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/30 10:17
"""
# 输出前n质数，注意性能
import math

from utils import time_this


@time_this()
def primes(n):
    """
    10000 总用时: 3.548116 s
    """
    tmp = []
    i = 0
    num = 1
    while i < n:
        if num >= 3:
            num += 2
        else:
            num += 1
        div_num = 2

        while div_num < int(math.sqrt(num)):
            if num % div_num == 0:
                break
            div_num += 1
        else:
            i += 1
            tmp.append(i)
            print(i, ':', num)


""" 统计所有小于非负整数 n 的质数的数量。
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


def count_primie(n):
    pass

if __name__ == '__main__':
    primes(10000)
