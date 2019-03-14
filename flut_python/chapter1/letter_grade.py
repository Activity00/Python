# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-11 上午8:56
"""
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


if __name__ == '__main__':
    results = [grade(score) for score in [33, 44, 99, 89, 90, 100]]
    print(results)