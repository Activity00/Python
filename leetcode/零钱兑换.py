# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/7 14:43
"""
"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
"""


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [0] * amount
    for i in range(1, amount):
        dp[i] = min([dp[i-j]+1 for j in coins if i-j >= 0], default=-1)
    return dp[-1]

if __name__ == '__main__':
    print(coinChange([1, 2, 5], 11))
