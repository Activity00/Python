# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/30 9:41
"""

import heapq
heapq.heapify()


def third_max(nums):
    t = list(set(nums))
    if len(t) < 3:
        return max(nums)
    t.sort(reverse=True)
    return t[2]

if __name__ == '__main__':
    pass
