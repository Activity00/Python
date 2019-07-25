import bisect


def insert_sort(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        i = j - 1
        target = bisect.bisect(nums[0:j], key)
        while target <= i:
            nums[i+1] = nums[i]
            i -= 1
        nums[i+1] = key


def test():
    nums_list = [1, 4, 7, 2, 5, 8]
    insert_sort(nums_list)
    print(nums_list)


if __name__ == '__main__':
    test()
