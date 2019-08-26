
def partition(nums, p, r):
    x = nums[r]
    i = p
    for j in range(p, r):
        if nums[j] < x:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def quick_sort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quick_sort(nums, p, q-1)
        quick_sort(nums, q+1, r)


def test():
    nums = [1, 7, 4, 2, 5, 8, 3]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)


if __name__ == '__main__':
    test()
