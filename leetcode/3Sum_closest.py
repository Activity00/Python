# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-4 上午11:18
"""
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = len(nums)
        num = nums[0] + nums[1] + nums[count-1]
        _min = abs(num - target)
        for i in range(count-2):
            j = i + 1
            k = count - 1

            if nums[i] + nums[k] + nums[k - 1] - target < 0:
                if abs(nums[i] + nums[k] + nums[k - 1] - target) < _min:
                    num = nums[i] + nums[k] + nums[k - 1]
                    _min = abs(nums[i] + nums[k] + nums[k - 1] - target)
                elif nums[i] + nums[k] + nums[k - 1] - target == 0:
                    return num
                continue

            while j < k:
                _sum = sum([nums[i],  nums[j], nums[k]])
                s = _sum - target
                abs_s = abs(s)
                if abs_s < _min:
                    num = _sum
                    _min = abs_s

                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    return num
        return num


def test_case():
    """
    >>> s = Solution()
    >>> s.threeSumClosest([-1, 2, 1, -4], 1)
    2
    """
    pass


if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([-1, 2, 1, -4], 1)
    import doctest
    doctest.testmod()
