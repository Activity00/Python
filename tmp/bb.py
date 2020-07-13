def insert_sort(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        i = j - 1

        while i >= 0 and nums[i] > key:
            nums[i + 1] = nums[i]
            i = i - 1
        nums[i + 1] = key


if __name__ == '__main__':
    a = [1, 3, 7, 2, 5, 8]
    insert_sort(a)
    print(a)
