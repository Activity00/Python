# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/30 10:04
"""
import random

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


def kmax(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]


import heapq


def kmax2(nums, k):
    return heapq.nlargest(k, nums)[-1]


def partication(nums, p, r):
    i = p
    for j in range(p, r):
        if nums[j] > nums[r]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def max_k(nums, p, r, k):
    q = partication(nums, p, r)
    if k - 1 == q:
        return nums[:q+1]
    if q > k - 1:
        return max_k(nums, p, q - 1, k)
    else:
        return max_k(nums, q + 1, r, k)


if __name__ == '__main__':
    nums = random.sample(range(10), 10)
    print(nums)
    print(max_k(nums, 0, len(nums) - 1, 3))
