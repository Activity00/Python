# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/24 17:13
"""
import doctest


def length_of_sub_str(s):
    """
    # 给定一个字符串，找出不含有重复字符的最长子串的长度。
    >>> length_of_sub_str('abcabcbb')
    3
    >>> length_of_sub_str('bbbbb')
    1
    >>> length_of_sub_str('pwwkew')
    3
    """
    dp, max_v, j = {}, 0, -1
    for i, c in enumerate(s):
        if c in dp:
            j = max(j, dp[c])
        dp[c], max_v = i, max(max_v, i - j)
    return max_v


if __name__ == '__main__':
    doctest.testmod()

