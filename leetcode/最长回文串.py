# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/2 11:24
"""

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    s_set = set([x for x in s])
    s_len = len(s)
    count = 0

    for x in s_set:
        if s.count(x) % 2 != 0:  # 判断有多少个基数对
            count += 1

    if count == 0:
        return s_len  # 全是偶数对，则本身是最长回文数
    else:
        return s_len - count + 1






if __name__ == '__main__':
    print(longestPalindrome('babad'))
