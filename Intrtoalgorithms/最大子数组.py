# coding: utf-8

"""
@author: 武明辉
@time: 18-8-31 上午8:39
"""

# ******************暴力计算*************************


def find_max_subarry_violent(nums):
    """
    >>> nums = [1,-2,3,10,-4,7,2,-48]
    >>> find_max_subarry_violent(nums)
    (2, 6, 18)
    >>> nums = [3,-1, 5, -1, 9, -20, 21, -20, 20, 21]
    >>> find_max_array_n_time(nums)
    (6, 9, 42)
    """
    count = len(nums)
    mx = nums[0]
    left = right = 0
    for i in range(count):
        for j in range(i, count):
            sm = sum(nums[i:j+1])
            if sm > mx:
                mx = sm
                left = i
                right = j
    return left, right, mx


# ******************分治递归*************************


def find_cross_mid(nums, p, r, m):
    """
    >>> nums = [1, -3, 7, 2, -5, 8]
    >>> find_cross_mid(nums, 0, len(nums)-1, (len(nums)-1)//2)
    (2, 5, 12)
    >>> find_cross_mid([3, -1, 7, 2, 5, 8], 0, 5, 2)
    (0, 5, 24)
    """
    tl = m
    lmax = ltmp = nums[m]
    for i in range(m-1, p-1, -1):
        ltmp += nums[i]
        if nums[i] > 0 and ltmp > lmax:
            lmax = ltmp
            tl = i

    tr = m + 1
    rmax = rtmp = nums[tr]
    for i in range(m+2, r+1):
        rtmp += nums[i]
        if nums[i] > 0 and rtmp > rmax:
            rmax = rtmp
            tr = i

    return tl, tr, lmax + rmax


def find_max_subarry(nums, p, r):
    """
    >>> a = [3, -1, 7, 2, 5, 8]
    >>> print(find_max_subarry(a, 0, len(a)-1))
    (0, 5, 24)
    """
    if p == r:
        return p, p, nums[p]
    m = (p + r) // 2
    ll, lr, lsum = find_max_subarry(nums, p, m)
    rl, rr, rsum = find_max_subarry(nums, m+1, r)
    ml, mr, msum = find_cross_mid(nums, p, r, m)
    tsum, tl, tr = lsum, ll, lr
    if rsum > lsum:
        tsum, tl, tr = rsum, rl, rr
    if msum > tsum:
        tsum, tl, tr = msum, ml, mr
    return tl, tr, tsum


# *******************线性时间复杂度**************************

def find_max_subarry_n(nums):
    mx = tmp = nums[0]
    for i in range(1, len(nums)):
        tmp = tmp + nums[i] if tmp > 0 else nums[i]
        mx = tmp if tmp > mx else mx
    return mx


"""
线性时间解决
"""


def find_max_array_n_time(nums):
    """
    >>> nums = [1,-2,3,10,-4,7,2,-48]
    >>> find_max_array_n_time(nums)
    (2, 6, 18)
    >>> nums = [3,-1, 5, -1, 9, -20, 21, -20, 20, 21]
    >>> find_max_array_n_time(nums)
    (6, 9, 42)
    """
    mx = boundry = nums[0]
    left = right = 0

    for i in range(1, len(nums)):
        if boundry > 0:
            boundry += nums[i]
        else:
            boundry = nums[i]
            left = i
        if boundry > mx:
            right = i
            mx = boundry

    return left, right, mx


"""
动态规划解决
"""


def find_max_array_dp(nums):
    """
    >>> nums = [1,-2,3,10,-4,7,2,-48]
    >>> find_max_array_dp(nums)
    (2, 6, 18)
    >>> nums = [3,-1, 5, -1, 9, -20, 21, -20, 20, 21]
    >>> find_max_array_dp(nums)
    (6, 9, 42)
    """

    left = right = 0
    mx = nums[0]
    dp = [0]* len(nums)
    dp[0] = nums[0]
    tmp = 0
    for i in range(1, len(nums)):
        if dp[i-1] < 0:
            dp[i] = dp[i] = nums[i]
            tmp = i
        else:
            dp[i] = nums[i] + dp[i-1]
        if dp[i] > mx:
            mx = dp[i]
            left = tmp
            right = i
    return left, right, mx


if __name__ == '__main__':
    import doctest
    doctest.testmod()

