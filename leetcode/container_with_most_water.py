# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-4 上午10:11
"""

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        mx = 0
        while i < j:
            tmp = (j-i) * min(height[i], height[j])
            mx = tmp if tmp > mx else mx
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return mx

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        mx = 0
        while i < j:
            tmp = (j-i) * min(height[i], height[j])
            mx = tmp if tmp > mx else mx

            if height[i] > height[j]:
                k = height[j]
                j -= 1
                while i < j and height[j] < k:
                    j -= 1
            else:
                k = height[i]
                i += 1
                while i < j and height[i] < k:
                    i += 1
        return mx


def test_case():
    """
    >>> s = Solution()
    >>> h = [1,8,6,2,5,4,8,3,7]
    >>> s.maxArea(h)
    49
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
