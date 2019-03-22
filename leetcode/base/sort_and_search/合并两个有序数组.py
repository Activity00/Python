# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-21 下午9:58
"""
"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        while index2 >= 0:
            if index1 < 0:
                nums1[0:index2 + 1] = nums2[0:index2 + 1]
                break

            if nums1[index1] >= nums2[index2]:
                nums1[index1 + index2 + 1] = nums1[index1]
                index1 -= 1
            else:
                nums1[index1 + index2 + 1] = nums2[index2]
                index2 -= 1

    def merge1(self, nums1, m, nums2, n):
        nums1[m:m+n] = nums2[:n]
        nums1.sort()


if __name__ == '__main__':
    pass
