# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/31 19:47
"""
"""
给定一个字符串，找出不含有重复字符的最长子串的长度。
示例：
给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""


def mlengthofstr(s):
    ma = 1
    i = 0
    j = 1
    st = set()

    while i < len(s) and j < len(s):
        if s[i] != s[j]:
            j += 1
            ma += 1
        else:
            if j - i + 1 > ma:
                ma = j - i + 1
            i = j
            j += 1
    return ma

if __name__ == '__main__':
    x = mlengthofstr('abcabcbb')
    print(x)
