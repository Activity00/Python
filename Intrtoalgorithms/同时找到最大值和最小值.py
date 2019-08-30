def find_max_min(nums):
    if len(nums) % 2 == 0:
        if nums[0] > nums[1]:
            mx = nums[1]
            mi = nums[0]
        else:
            mx = nums[0]
            mi = nums[1]

        start = 3
    else:
        mi = mx = nums[0]
        start = 2

    for i in range(start, len(nums)):
        if nums[i - 1] > nums[i]:
            if nums[i - 1] > mx:
                mx = nums[i - 1]
            if nums[i] < mi:
                mi = nums[i]
        else:
            if nums[i - 1] < mi:
                mi = nums[i - 1]
            if nums[i] > mx:
                mx = nums[i]

    return mi, mx


def test():
    nums = [1, 3, 5, 7, 2, 4, 6, 8, 0]
    print(find_max_min(nums))


if __name__ == '__main__':
    test()
