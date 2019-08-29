
def partition(nums, p, r):
    i = p
    for j in range(p, r):
        if nums[j] > nums[r]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def found_kth_r(nums, p, r, k):
    q = partition(nums, p, r)
    if q == k:
        return nums[q]
    elif q < k:
        return found_kth_r(nums, q+1, r, k)
    else:
        return found_kth_r(nums, p, q-1, k)


def found_kth(nums, k):
    return found_kth_r(nums, 0, len(nums) - 1, k-1)


def test():
    a = [1, 4, 7, 2, 5, 8]
    print(found_kth(a, 2))


if __name__ == '__main__':
    test()
