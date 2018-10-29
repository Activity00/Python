# coding: utf-8
import doctest


"""
@author: 武明辉
@time: 18-10-29 下午5:31
"""


def square_matrix_multiply(a, b):
    """
    >>> a = [[ 0,  1,  2,  3], [ 4,  5,  6,  7], [ 8,  9, 10, 11], [12, 13, 14, 15]]
    >>> square_matrix_multiply(a, a)
    [[56, 62, 68, 74], [152, 174, 196, 218], [248, 286, 324, 362], [344, 398, 452, 506]]
    """
    n = len(a)
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sm = 0
            for k in range(n):
                sm += (a[i][k] * b[k][j])
            c[i][j] = sm

    return c


if __name__ == '__main__':
    doctest.testmod()

