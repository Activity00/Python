# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-10 下午4:25
"""
"""
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        for i, item in enumerate(s):
            if dct[item] == 1:
                return i
        else:
            return -1

    def firstUniqChar2(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.find(l) != -1 and s.find(l) == s.rfind(l)]
        return min(index) if len(index) > 0 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("dddccdbba"))


