# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-19 下午9:12
"""
import re

"""
 验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """128ms"""
        t = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        return list(t) == list(reversed(t))

    def isPalindrome1(self, s: str) -> bool:
        """96 ms"""
        t = [i for i in s if i.isalpha() or i.isdigit()]
        i = 0
        j = len(t) - 1
        m = len(t) // 2
        while i < m <= j:
            if t[i].lower() != t[j].lower():
                break
            i += 1
            j -= 1
        else:
            return True
        return False

    def isPalindromel(self, s: str) -> bool:
        """72ms"""
        alphanumeric = re.sub("[^A-Za-z0-9]+", "", s).lower()
        print(alphanumeric)
        return alphanumeric == alphanumeric[::-1]


if __name__ == '__main__':
    s = Solution()
    ret = s.isPalindrome1("A man, a plan, a canal: Panama")
    print(ret)
