def insert_sort(nums, n):
    if n == 0:
        return
    key = nums[n]
    insert_sort(nums, n-1)
    i = n - 1
    while i >= 0 and nums[i] > key:
        nums[i+1] = nums[i]
        i -= 1
    nums[i+1] = key


def test():
    nums_list = [1, 4, 7, 2, 5, 8]
    insert_sort(nums_list, len(nums_list)-1)
    print(nums_list)


if __name__ == '__main__':
    test()
