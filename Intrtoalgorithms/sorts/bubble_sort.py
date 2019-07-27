# coding: utf-8

"""
@author: 武明辉 
@time: 19-7-27 上午11:34
"""


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(1, len(nums) - i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]


def test():
    nums_list = [1, 4, 7, 2, 5, 8]
    bubble_sort(nums_list)
    print(nums_list)


if __name__ == '__main__':
    test()
