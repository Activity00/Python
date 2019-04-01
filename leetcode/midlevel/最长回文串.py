"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxl = 0
        start = 0
        for i in range(len(s)):
            if i - maxl >= 1 and s[i-maxl-1: i + 1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start+maxl]

    def longestPalindrome2(self, s: str) -> str:
        length = len(s)
        if length < 2 or s == s[::-1]:
            return s
        max_len, begin = 1, 0
        for i in range(1, length):
            odd = s[i - max_len - 1:i + 1]
            even = s[i - max_len:i + 1]
            if i - max_len >= 1 and odd == odd[::-1]:
                begin = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                begin = i - max_len
                max_len += 1
        return s[begin:begin + max_len]

# 答案参考 https://blog.csdn.net/asd136912/article/details/78987624


