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


def merge_list(l, r):
    l_l = r_l = 0
    result = []
    while l_l < len(l) and r_l < len(r):
        if l[l_l] > r[r_l]:
            result.append(r[r_l])
        else:
            result.append(l[l_l])
        l_l += 1
        r_l += 1
    if l_l:
        result += l[l_l:]
    else:
        result += r[r_l]
    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    m = len(nums) // 2
    left = nums[:m]
    right = nums[m:]
    l = merge_sort(left)
    r = merge_sort(right)
    return merge_list(l, r)


if __name__ == '__main__':
    doctest.testmod()
    print(merge_sort([1,3,7,2,5,8]))
