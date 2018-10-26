# coding: utf-8

"""
@author: 武明辉 
@time: 18-10-26 下午3:35
"""
import operator
import random
import doctest


def insert_sort(nums):
    """
    >>> nums = random.sample(range(10), 10)
    >>> target = insert_sort(nums)
    >>> operator.eq(target, sorted(nums))
    True
    """
    for i in range(1, len(nums)):
        k = nums[i]
        j = i
        while j > 0 and k < nums[j - 1]:
            nums[j] = nums[j - 1]
            nums[j - 1] = k
            j -= 1

    return nums


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


if __name__ == '__main__':
    doctest.testmod()
