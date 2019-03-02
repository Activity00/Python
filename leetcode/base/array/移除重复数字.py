# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-2 上午9:47
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        相对低效
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                i += 1
            else:
                nums.remove(nums[i+1])
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        """
        不管后面的只返回数字结果
        """
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates2([1, 1, 1, 2, 2, 3]))
