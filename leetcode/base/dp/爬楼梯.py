"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in {1, 2}:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(self, n: int) -> int:
        if n in {1, 2}:
            return n
        a = 1
        b = 2
        for _ in range(n-2):
            t = a + b
            a = b
            b = t
        return b

    def climbStairs2(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n):
            a = a + b
            a, b = b, a
        return b

