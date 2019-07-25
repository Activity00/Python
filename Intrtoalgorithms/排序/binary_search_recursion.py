def binary_search(nums, p, r, key):
    if p >= r:
        return None
    q = (p + r) // 2
    if key == nums[q]:
        return q
    if key < nums[q]:
        binary_search(nums, p, q - 1, key)
    else:
        binary_search(nums, q + 1, r, key)


def test():
    nums = [1, 2, 3, 4, 5, 6]
    print(binary_search(nums, 0, len(nums) - 1, 3))
    print(binary_search(nums, 0, len(nums) - 1, 10))


if __name__ == '__main__':
    test()
