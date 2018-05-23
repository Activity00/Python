# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/23 18:48
"""

"""
找钱问题 1 3 5 最少张数
"""


def dp_plus(ii):
    """
        >>> dp_plus(1)
        1
        >>> dp_plus(10)
        2
        >>> dp_plus(11)
        3
    """
    ret = [0] * (ii + 1)
    for i in range(ii + 1):
        ret[i] = min([ret[i-j] + 1 for j in (1, 3, 5) if i >= j], default=0)
    return ret[ii]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
