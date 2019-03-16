

"""
计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        ret = 0
        first = True
        i = 2
        while i < n:
            for j in range(2, int(i**0.5)):
                if i % j == 0:
                    break
            else:
                ret += 1
            if first:
                i += 1
                first = False
            else:
                i += 2
        return ret
