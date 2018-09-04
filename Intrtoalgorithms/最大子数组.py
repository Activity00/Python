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
            ltemp += nums[i]
            lt = i

    rmx = nums[m+1]
    rtemp = nums[m+1]
    rt = m + 1
    for i in range(m+2, r+1):
        if nums[i] + rtemp > rmx:
            rmx = nums[i] + rtemp
            rtemp += nums[i]
            rt = i

    return (lt, rt), lmx + rmx


def find_max_subarray(nums, p, r):
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


# *******************线性时间复杂度**************************

def find_max_subarry_n(nums):
    mx = tmp = nums[0]
    for i in range(1, len(nums)):
        tmp = tmp + nums[i] if tmp > 0 else nums[i]
        mx = tmp if tmp > mx else mx
    return mx


def find_max_subarry_n_plus(nums):
    mx = tmp = nums[0]
    l = r = 0
    for i in range(1, len(nums)):
        if tmp > 0:
            tmp += nums[i]
        else:
            tmp = nums[i]
            l = i
        if tmp > mx:
            mx = tmp
            r = i
    return (l, r), mx


def test_case():
    """
    >>> a = [1, 3, 7, 2, 5, 8]
    >>> print(find_max_subarry_n(a))
    26
    >>> a = [1, 3, 7, 2, 5, 8]
    >>> print(find_max_subarry_n_plus(a))
    ((0, 5), 26)

    >>> a = [1, 3, 7, 2, 5, 8]
    >>> find_max_subarray(a, 0, len(a)-1)
    ((0, 5), 26)
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(find_max_subarry_n([3, -1, 7, 2, 5, 8]))
    a = [1, 3, 7, 2, 5, 8]
    print(cross_mid(a, 0, 5, 3))
