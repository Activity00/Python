# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/10 10:49
"""
import doctest

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer 
overflows.
"""


class Solution:
    def reverse(self, x):
        """
        >>> s = Solution()
        >>> s.reverse(123)
        321
        >>> s.reverse(-123)
        -321
        >>> s.reverse(120)
        21
        """
        ret = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x:
            x, y = divmod(x, 10)
            ret = ret * 10 + y
        return ret * sign if -2 ** 31 <= ret <= 2 ** 31 - 1 else 0

    def reverse2(self, x):
        """
        使用中间字符串
        """
        """
        >>> s = Solution()
        >>> s.reverse(123)
        321
        >>> s.reverse(-123)
        -321
        >>> s.reverse(120)
        21
        """
        ret = int(str(abs(x))[::-1])
        return ret * ((x > 0) - (x < 0)) if -2 ** 31 <= ret <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    doctest.testmod()
