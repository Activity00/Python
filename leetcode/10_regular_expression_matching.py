# coding: utf-8

"""
@author: 武明辉 
@time: 18-11-6 下午6:51
"""
import doctest

"""
Given an input string (s) and a p (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:

    def isMatch(self, s, p):
        # 递归解法
        """
        >>> s = Solution()
        >>> s.isMatch('aa', 'a')
        False
        >>> s.isMatch('aa', 'a*')
        True
        >>> s.isMatch('ab', '.*')
        True
        >>> s.isMatch('aab', 'c*a*b')
        True
        >>> s.isMatch('mississippi', 'mis*is*p*.')
        False
        # 超时 >>> s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
        # False
        """
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])


    # def isMatchdp(self, s, p):
    #     # 动态规划解法
    #     memo = {}
    #
    #     def dp(i, j):
    #         if (i, j) not in memo:
    #             if j == len(p):
    #                 ans = i == len(s)
    #             else:
    #                 first_match = i < len(s) and p[j] in {s[i], '.'}
    #                 if j + 1 < len(p) and p[j + 1] == '*':
    #                     ans = dp(i, j + 2) or first_match and dp(i + 1, j)
    #                 else:
    #                     ans = first_match and dp(i + 1, j + 1)
    #
    #             memo[i, j] = ans
    #         return memo[i, j]
    #
    #     return dp(0, 0)
    #
    # def isMatchbottom_up(self, s, p):
    #         # 动态规划解法
    #     dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    #
    #     dp[-1][-1] = True
    #     for i in range(len(s), -1, -1):
    #         for j in range(len(p) - 1, -1, -1):
    #             first_match = i < len(s) and p[j] in {s[i], '.'}
    #             if j + 1 < len(p) and p[j + 1] == '*':
    #                 dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
    #             else:
    #                 dp[i][j] = first_match and dp[i + 1][j + 1]
    #
    #     return dp[0][0]


if __name__ == '__main__':
    doctest.testmod()

