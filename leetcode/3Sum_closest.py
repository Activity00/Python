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


def test_case():
    """
    >>> s = Solution()
    >>> s.threeSumClosest([-1, 2, 1, -4], 1)
    2
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
