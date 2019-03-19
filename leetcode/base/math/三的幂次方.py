"""
 3的幂
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？
"""
import math
import sys


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1 or int(n) < n:
            return False
        return self.isPowerOfThree(n / 3)

    def isPowerOfThree2(self, n: int) -> bool:
        while 1 <= n == int(n):
            if n == 1:
                return True
            n = n / 3
        return False

    def isPowerOfThree3(self, n: int) -> bool:
        """
        ?
        :param n:
        :return:
        """
        if n < 1:
            return False
        return 3 ** 19 % n == 0
