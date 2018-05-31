# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/29 10:06
"""
import doctest

"""
选择排序: 从数组中挑选最大/小一个数字，次大/小数字，遍历所有
"""


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


"""
选择排序 记录下标不每次都交换
"""


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

"""
冒泡排序, 相邻两两交换把最大/小放在后面
"""


def bubble_sort(nums):
    """
    >>> bubble_sort([1, 4, 7, 2, 5, 8])
    [1, 2, 4, 5, 7, 8]
    """
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def partication(nums, p, r):
    i = p
    for j in range(p, r+1):
        if nums[j] < nums[r]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def fast_sort(nums, p, r):
    """
    >>> x = [1,3,5,7,2,4,6,8]
    >>> fast_sort(x, 0, len(x) - 1)
    >>> x
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if p < r:
        q = partication(nums, p, r)
        fast_sort(nums, p, q-1)
        fast_sort(nums, q+1, r)


if __name__ == '__main__':
    doctest.testmod()

