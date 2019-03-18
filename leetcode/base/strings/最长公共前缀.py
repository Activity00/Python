""" 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        count = len(strs)
        m = len(strs[0])
        for i in range(count):
            if len(strs[i]) < m:
                m = len(strs[i])
        flag = False
        i = 0
        while i < m:
            for j in range(1, count):
                if strs[j][i] != strs[0][i]:
                    flag = True
                    break
            if flag:
                break
            i += 1
        return strs[0][:i]


if __name__ == '__main__':
    s = Solution()
    ret = s.longestCommonPrefix(["dog", "racecar", "car"])
    print(ret)
