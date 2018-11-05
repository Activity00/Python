# coding: utf-8

"""
@author: 武明辉 
@time: 18-11-1 下午3:19
"""
import doctest

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:

    def longestPalindrome(self, s):
        """
        # 1580 ms
        """
        if not s:
            return s
        ret = ''
        start = end = 0
        for i in range(len(s)):
            j = k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                start, end = j, k
                j -= 1
                k += 1
            if end + 1 - start > len(ret):
                ret = s[start:end+1]
            j = k = i
            while j >= 0 and k+1 < len(s) and s[j] == s[k+1]:
                start, end = j, k+1
                j -= 1
                k += 1
            if end + 1 - start > len(ret):
                ret = s[start:end + 1]

        return ret

    def net(self, s):
        ans = ''

        if not s:
            return ans
        if s == s[::-1]:
            return s

        i = 0
        k = 1

        for j in range(2, len(s) + 1):
            if j - k - 1 >= 1:
                t = s[j - k - 2:j]
                if t == t[::-1]:
                    i = j - k - 2
                    k += 2
                    continue
            if j - k - 1 >= 0:
                t = s[j - k - 1:j]
                if t == t[::-1]:
                    i = j - k - 1
                    k += 1

        return s[i:i + k]



if __name__ == '__main__':
    # doctest.testmod()
    s = Solution()
    print(s.longestPalindrome('aaaa'))
