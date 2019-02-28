def partication(nums, p, r):
    i = p
    for j in range(p, r):
        if nums[j] <= nums[r]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def topk(nums, k):
    low = 0
    high = len(nums)-1
    q = partication(nums, low, high)
    while q != k - 1:
        if q < k - 1:
            low = q + 1
        else:
            high = q - 1
        q = partication(nums, low, high)
