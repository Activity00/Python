import operator
import random


def merge(nums, p, q, r):
    global count
    print(f'merge {nums[p:q + 1]} {nums[q + 1:r + 1]}')
    left = nums[p:q + 1]
    right = nums[q + 1:r + 1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(p, r + 1):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            count += 1
            nums[k] = right[j]
            j += 1

    print(f'result: {nums[p:r + 1]}')


def merge_sort(nums, p, r):
    """
    >>> nums = random.sample(range(10), 10)
    >>> ret = sorted(nums)
    >>> merge_sort(nums, 0, len(nums)-1)
    >>> operator.eq(ret, nums)
    True
    """
    if p < r:
        q = (p + r) // 2
        merge_sort(nums, p, q)
        merge_sort(nums, q + 1, r)
        merge(nums, p, q, r)


if __name__ == '__main__':
    count = 0
    nums_list = [2, 3, 8, 6, 1]
    merge_sort(nums_list, 0, len(nums_list) - 1)
    print(nums_list)
    print(count)