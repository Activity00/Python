# coding: utf-8

"""
@author: 武明辉 
@time: 18-10-30 下午4:25
"""
import copy
import doctest

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substri
"""


class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        >>> s = Solution()
        >>> s.lengthOfLongestSubstring('abcabcbb')
        3
        >>> s.lengthOfLongestSubstring('bbbbb')
        1
        >>> s.lengthOfLongestSubstring('pwwkew')
        3
        """
        dic = {}
        mx = 0
        start = 0
        for i in range(0, len(s)):
            if s[i] in dic:
                start = dic[s[i]] + 1
            dic[s[i]] = i
            mx = max(i - start + 1, mx)
        return mx

    def lengthOfLongestSubstring_net(self, s):
        """
        >>> s = Solution()
        >>> s.lengthOfLongestSubstring_net('abcabcbb')
        3
        >>> s.lengthOfLongestSubstring_net('bbbbb')
        1
        >>> s.lengthOfLongestSubstring_net('pwwkew')
        3
        """
        dic = {}
        start = res = 0

        for i in range(len(s)):
            if s[i] in dic:
                start = max(start, dic[s[i]] + 1)

            dic[s[i]] = i
            res = max(res, i - start + 1)
        return res

    def func(self, s):
        """
        >>> s = Solution()
        >>> s.func('abcabcbb')
        3
        >>> s.func('bbbbb')
        1
        >>> s.func('pwwkew')
        3
        """
        dui_str = []
        dui_str_2 = []
        for i in s:
            if i in dui_str:
                if len(dui_str_2) < len(dui_str):
                    dui_str_2 = copy.deepcopy(dui_str)
                while True:
                    if i == dui_str[0]:
                        dui_str.pop(0)
                        dui_str.append(i)
                        break
                    else:
                        dui_str.pop(0)
            else:
                dui_str.append(i)
        if len(dui_str_2) >= len(dui_str):
            return len(dui_str_2)
        else:
            return len(dui_str)


if __name__ == '__main__':
    doctest.testmod()
