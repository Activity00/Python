# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/23 18:48
"""

"""
找钱问题 1 3 5 最少张数
"""


def dp_money(ii):
    """
        >>> dp_money(1)
        1
        >>> dp_money(10)
        2
        >>> dp_money(11)
        3
    """
    ret = [0] * (ii + 1)
    for i in range(ii + 1):
        ret[i] = min([ret[i-j] + 1 for j in (1, 3, 5) if i >= j], default=0)
    return ret[ii]


"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""


def dp_jump(nums):
    """
    >>> dp_jump([2, 3, 1, 1, 4])
    2
    >>> dp_jump([1, 1, 7, 5, 8, 4])
    3
    """
    ret = [0] * len(nums)
    for i in range(1, len(nums)):
        ret[i] = min([ret[j] + 1 for j in range(i) if 0 <= i-j <= nums[j]], default=0)
    return ret[len(nums)-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

