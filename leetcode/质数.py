# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/30 10:17
"""
# 输出前n质数，注意性能


def primes(n):
    i = 0
    num = 1
    while i <= n:
        num += 1
        div_num = 2
        while div_num < num:
            if num % div_num == 0:
                break
            div_num += 1
        else:
            i += 1
            print(i, ':', num)

if __name__ == '__main__':
    primes(1000)
