

def merge(nums, p, q, r):
    print(f'merge {nums[p:q + 1]} {nums[q + 1:r + 1]}')
    left = nums[p:q+1]
    right = nums[q+1:r+1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(p, r + 1):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1

    print(f'result: {nums[p:r + 1]}')


def merge_sort(nums, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(nums, p, q)
        merge_sort(nums, q + 1, r)
        merge(nums, p, q, r)


nums = [5, 2, 4, 7, 1, 3, 2, 6]
merge_sort(nums, 0, len(nums)-1)
print(nums)
