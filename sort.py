# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/29 10:06
"""
import doctest


def select_sort(nums):
    """
    >>> select_sort([1, 4, 7, 2, 5, 8])
    [1, 2, 4, 5, 7, 8]
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def select_sort_p(nums):
    """
    >>> select_sort_p([1, 4, 7, 2, 5, 8])
    [1, 2, 4, 5, 7, 8]
    """
    count = len(nums)
    for i in range(count):
        m = i
        for j in range(i+1, count):
            if nums[m] > nums[j]:
                m = j
        nums[i], nums[m] = nums[m], nums[i]
    return nums


def bubble_sort(nums):
    """
    >>> bubble_sort([1, 4, 7, 2, 5, 8])
    [1, 2, 4, 5, 7, 8]
    """
    for i in range(len(nums)):
        for j in range(len(nums) - i -1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == '__main__':
    doctest.testmod()

