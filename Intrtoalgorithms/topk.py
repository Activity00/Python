def partition(nums, p, r):
    i = p
    for j in range(p, r + 1):
        if nums[j] > nums[r]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[r], nums[i] = nums[i], nums[r]
    return i


def top_k(nums, k):
    low = 0
    high = len(nums)-1
    q = partition(nums, low, high)
    while q != k - 1:
        if q < k - 1:
            low = q + 1
        else:
            high = q - 1
        q = partition(nums, low, high)
    return nums[q]


if __name__ == '__main__':
    ns = [1, 4, 7, 2, 5, 8]
    x = top_k(ns, 2)
    print(x)
    print(ns)
