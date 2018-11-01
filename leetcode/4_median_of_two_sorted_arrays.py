# coding: utf-8

"""
@author: 武明辉 
@time: 18-10-31 上午10:37
"""
import doctest

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 104ms
        """
        >>> s = Solution()
        >>> s.findMedianSortedArrays([1, 2], [3, 4])
        2.5
        >>> s.findMedianSortedArrays([1, 3], [2])
        2
        """
        c1, c2 = len(nums1), len(nums2)
        count = c1 + c2
        a, b = divmod(count, 2)
        i = j = k = 0
        res = []

        while k < a+1:
            if i < c1 and j < c2:
                if nums1[i] < nums2[j]:
                    v = nums1[i]
                    i += 1
                else:
                    v = nums2[j]
                    j += 1
            elif i < c1:
                v = nums1[i]
                i += 1
            else:
                v = nums2[j]
                j += 1
            res.append(v)
            k += 1
        return (res[-1] + res[-2]) / 2 if b == 0 else res[-1]



    def findMedianSortedArrays_sort(self, nums1, nums2):
        # 144 ms
        """
        >>> s = Solution()
        >>> s.findMedianSortedArrays([1, 2], [3, 4])
        2.5
        """
        nums1 = sorted(nums1 + nums2)
        a, b = divmod(len(nums1), 2)
        return sum(nums1[a-1:a+1])/2 if b == 0 else nums1[a]


if __name__ == '__main__':
    doctest.testmod()
