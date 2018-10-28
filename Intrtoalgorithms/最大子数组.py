# coding: utf-8

"""
@author: 武明辉 
@time: 18-8-31 上午8:39
"""

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
