
def binary_search(nums, key):
    p = 0
    r = len(nums) - 1
    while p <= r:
        q = (p + r) // 2
        if nums[q] == key:
            return q
        if nums[q] < key:
            p = q + 1
        else:
            r = q - 1
    else:
        return None


def test():
    nums_list = [1, 4, 7, 2, 5, 8]
    print(binary_search(nums_list, 7))
    print(binary_search(nums_list, 17))


if __name__ == '__main__':
    test()
