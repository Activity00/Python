# coding: utf-8

"""
@author: 武明辉 
@time: 19-1-7 下午5:55
"""
import doctest
import random
import operator


def bubble_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums)
    >>> operator.eq(bubble_sort(nums), target)
    True
    """
    count = len(nums)
    for i in range(count):
        for j in range(1, count-i):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


if __name__ == '__main__':
    nums = random.sample(range(10), 10)
    target = sorted(nums)
    print(bubble_sort(nums))

    doctest.testmod()
