import doctest
import random
import operator


def partication(nums, p, r):
    i = p
    for j in range(p, r):
        if nums[j] < nums[r]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def quick_sort(nums, p, r):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums)
    >>> quick_sort(nums, 0, len(nums) - 1)
    >>> operator.eq(nums, target)
    True
    """
    if p < r:
        q = partication(nums, p, r)
        quick_sort(nums, p, q - 1)
        quick_sort(nums, q + 1, r)


def merge(l, r):
    ret = []
    while l and r:
        if l[0] > r[0]:
            ret.append(r.pop(0))
        else:
            ret.append(l.pop(0))
    if l:
        ret += l
    else:
        ret += r
    return ret


def merge_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = sorted(nums)
    >>> operator.eq(merge_sort(nums), target)
    True
    """
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    l = merge_sort(nums[:mid])
    r = merge_sort(nums[mid:])
    return merge(l, r)


if __name__ == '__main__':
    doctest.testmod()
