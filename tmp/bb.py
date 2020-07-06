def merge(nums, p, q, r):
    return p


def merge_sort(nums, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(nums, p, q)
        merge_sort(nums, q + 1, r)
        merge(nums, p, q, r)


def test():
    nums_list = [5, 2, 4, 7, 1, 3, 2, 6, 9, 10]
    # nums_list = [5, 2, 4]
    merge_sort(nums_list, 0, len(nums_list) - 1)
    print(nums_list)


if __name__ == '__main__':
    test()
