# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/29 10:06
"""
import operator
import random
import doctest

"""
选择排序: 从数组中挑选最大/小一个数字，次大/小数字，遍历所有
"""


def select_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = select_sort(nums)
    >>> operator.eq(target, sorted(nums))
    True
    """
    count = len(nums)
    for i in range(count):
        for j in range(i+1, count):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


"""
选择排序优化 记录下标不每次都交换
"""


def select_sort_p(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = select_sort_p(nums)
    >>> operator.eq(target, sorted(nums))
    True
    """
    count = len(nums)
    for i in range(count):
        m = i
        for j in range(i+1, count):
            if nums[j] < nums[m]:
                m = j
        nums[i], nums[m] = nums[m], nums[i]
    return nums


"""
冒泡排序, 相邻两两交换把最大/小放在后面
"""


def buble_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = buble_sort(nums)
    >>> operator.eq(target, sorted(nums))
    True
    """
    count = len(nums)
    for i in range(count):
        for j in range(count-i-1):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


"""
快速排序 两两分区分别排序
"""


def partication(nums, p, r):
    i = p
    for j in range(p, r+1):
        if nums[j] < nums[r]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[r], nums[i] = nums[i], nums[r]
    return i


def quick_sort(nums, p, r):
    """
    >>> nums = random.sample(range(10), 10)
    >>> quick_sort(nums, 0, len(nums)-1)
    >>> operator.eq(nums, sorted(nums))
    True
    """
    if p < r:
        q = partication(nums, p, r)
        quick_sort(nums, p, q-1)
        quick_sort(nums, q+1, r)

"""
归并排序 分治思想，一半一半分割最后合并
"""


def merge(l, r):
    ret = []
    while l and r:
        if l[0] > r[0]:
            ret.append(r.pop(0))
        else:
            ret.append(l.pop(0))
    if r:
        ret += r
    if l:
        ret += l
    return ret


def merge_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = merge_sort(nums)
    >>> operator.eq(target, sorted(nums))
    True
    """
    if len(nums) == 1:
        return nums

    q = len(nums) // 2
    l = merge_sort(nums[q:])
    r = merge_sort(nums[:q])
    return merge(l, r)


def merge2(nums, l, r):
    ret = []
    while l and r:
        if l[0] > r[0]:
            ret.append(r[0])
        else:
            ret.append(l[0])
    if r:
        ret += r
    else:
        ret += l
    return ret


"""
原址排序
"""


def merge_sort2(nums, p, r):
    """
    >>> nums = random.sample(range(10), 10)
    >>> ret = sorted(nums)
    >>> merge_sort2(nums, 0, len(nums))
    >>> operator.eq(ret, nums)
    True
    """
    if p == r:
        return nums[p]

    q = (p + r) // 2
    l = merge_sort2(nums, p, q)
    r = merge_sort2(nums, q, r)
    merge2(nums, l, r)
    return nums


"""
插入排序  类似扑克牌从没有排序牌中依次选一张排序
"""


def insert_sort(nums):
    """
    >>> insert_sort([1, 3, 7, 2, 5, 8])
    [1, 2, 3, 5, 7, 8]
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > key:
                nums[j+1] = nums[j]
                nums[j] = key
            j -= 1
    return nums


"""
插入排序递归实现
"""


def insert_sort_recursive(nums, p):
    """
    >>> a = [1, 3, 7, 2, 5, 8]
    >>> insert_sort_recursive(a, len(a)-1)
    >>> a
    [1, 2, 3, 5, 7, 8]
    """
    if p > 0:
        insert_sort_recursive(nums, p-1)
        insert(nums, p)


def insert(nums, p):
    key = nums[p]
    j = p - 1
    while j >= 0:
        if nums[j] > key:
            nums[j + 1] = nums[j]
            nums[j] = key
        j -= 1


"""
二分法优化while循环部分
"""


def insert_sort_p(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums)
    >>> operator.eq(insert_sort_p(nums), target)
    True
    """
    count = len(nums)
    for i in range(1, count):
        key = nums[i]
        j = i - 1
        st = 0
        while st <= j:
            mid = (st + j) // 2
            if nums[mid] > key:
                j = mid - 1
            else:
                st = mid + 1
        for k in range(i, st, -1):
            nums[k] = nums[k-1]

        nums[j+1] = key
    return nums


"""
希尔排序 插入排序增强版
"""


def shell_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = shell_sort(nums)
    >>> operator.eq(target, sorted(nums))
    True
    """
    count = len(nums)
    step = 2
    group = count // step
    while group > 0:
        for i in range(group):
            for j in range(i+group, count, group):
                key = nums[j]
                k = j
                while k > i and nums[k] < nums[k-group]:
                    nums[k] = nums[k-group]
                    nums[k-group] = key
                    k -= group

        group //= step
    return nums


'''
计数排序
'''


def counting_sort(nums):
    """
    >>> nums = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    >>> counting_sort(nums)
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 6]
    """
    temp_list = [0] * (max(nums)+1)
    ret_list = [0] * len(nums)
    for i in nums:
        temp_list[i] += 1

    for i in range(1, len(temp_list)):
        temp_list[i] += temp_list[i-1]

    for i in nums:
        ret_list[temp_list[i]-1] = i
        temp_list[i] -= 1
    return ret_list


"""
基数排序
"""


def radix_sort(nums, d=3):  # 默认三位数，如果是四位数，则d=4，以此类推
    """
    >>> a = [123, 789, 456]
    >>> radix_sort(a)
    [123, 456, 789]
    """
    ret = []
    for i in range(d):  # d轮排序
        s = [[] for _ in range(10)]  # 因每一位数字都是0~9，建10个桶
        for j in nums:
            s[int(j / (10 ** i)) % 10].append(j)
        ret = [a for b in s for a in b]
    return ret


"""
桶排序
"""


def bucket_sort(a):
    """
    >>> a = [123, 789, 456]
    >>> radix_sort(a)
    [123, 456, 789]
    """
    buckets = [0] * ((max(a) - min(a)) + 1)  # 初始化桶元素为0
    for i in range(len(a)):
        buckets[a[i] - min(a)] += 1  # 遍历数组a，在桶的相应位置累加值
    b = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            b += [i + min(a)] * buckets[i]
    return b


if __name__ == '__main__':
    doctest.testmod()
