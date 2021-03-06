"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = 0
        for i, n in enumerate(nums):
            ret += i - n
        return ret + len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
