# coding: utf-8

"""
@author: 武明辉 
@time: 19-1-7 下午5:55
"""
import doctest
import random
import operator


def insert_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums)
    >>> operator.eq(insert_sort(nums), target)
    True
    """
    count = len(nums)
    for i in range(1, count):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

    return nums


def insert_sort_p(nums):
    """
    二分法优化while循环部分
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums)
    >>> operator.eq(insert_sort_p(nums), target)
    True
    """
    count = len(nums)
    for i in range(1, count):
        key = nums[i]
        j = i - 1
        st = 0
        while st <= j:
            mid = (st + j) // 2
            if nums[mid] > key:
                j = mid - 1
            else:
                st = mid + 1
        for k in range(i, st, -1):
            nums[k] = nums[k-1]

        nums[j+1] = key
    return nums


def insert_sort_d(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums,reverse=True)
    >>> operator.eq(insert_sort_d(nums), target)
    True
    """
    count = len(nums)
    for i in range(1, count):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] < key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

    return nums


def select_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums,reverse=False)
    >>> operator.eq(select_sort(nums), target)
    True
    """
    count = len(nums)
    for i in range(count):
        for j in range(i+1, count):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == '__main__':
    nums = random.sample(range(10), 10)
    print(nums)
    target = sorted(nums)
    print(insert_sort_p(nums))
    doctest.testmod()
