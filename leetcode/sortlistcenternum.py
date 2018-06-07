# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/2 11:15
"""


def middle_num(nums1, nums2):
    l = nums1 + nums2
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

if __name__ == '__main__':
    print(middle_num([], [2, 3]))
