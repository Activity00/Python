# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-10 下午3:22
"""
from typing import List
import doctest
"""
 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


class Solution:
    """
    >>> s = Solution()
    >>> s.intersect([4, 9, 5], [9, 4, 9, 8, 4])
    [9, 4]
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ret = []
        for num in nums1:
            if d.get(num):
                d[num] += 1
            else:
                d[num] = 1
        for num in nums2:
            if num in d and d[num] > 0:
                ret.append(num)
                d[num] -= 1
        return ret

    def intersect2(self, nums1, nums2):
        """内部方法 """
        from collections import Counter
        return list((Counter(nums1) & Counter(nums2)).elements())


if __name__ == '__main__':
    doctest.testmod()
