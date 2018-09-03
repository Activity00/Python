# coding: utf-8

"""
@author: 武明辉 
@time: 18-8-31 上午8:39
"""

# ******************分治递归*************************


def cross_mid(nums, p, r, m):
    lmx = nums[m]
    ltemp = nums[m]
    lt = m
    for i in reversed(range(p, m)):
        if nums[i] + ltemp > lmx:
            lmx = nums[i] + ltemp
            lt = i

    rmx = nums[m+1]
    rtemp = nums[m+1]
    rt = m + 1
    for i in range(m+1, r):
        if nums[i] + rtemp > rmx:
            rmx = nums[i] + rtemp
            rt = i

    return (lt, rt), lmx + rmx


def find_max_subarray(nums, p, r):
    """
    >>> a = [1, 3, 7, 2, 5, 8]
    >>> find_max_subarray(a, 0, len(a)-1)
    ((1, 4), 17)
    """
    if p == r:
        return (p, r), nums[p]
    m = (p + r) // 2
    left = find_max_subarray(nums, p, m)
    right = find_max_subarray(nums, m+1, r)
    mid = cross_mid(nums, p, r, m)
    mx = left
    if right[1] > mx[1]:
        mx = right
    if mid[1] > mx[1]:
        mx = mid
    return mx


def find_max_subarry_n(nums):
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

