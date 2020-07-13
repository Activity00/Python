# -*-coding:utf-8-*-
# ！usr/bin/env python
'''
Created on 2017年4月19日

@author: 武明辉
'''


def insert_sort(lists):
    """插入排序"""
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if key < lists[j]:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


def bubble_sort(lists):
    """冒泡排序"""
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = list[j], list[i]
    return lists


def quick_sort(lists, left, right):
    """快速排序"""
    if left > right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] > key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


lists = [5, 4, 3, 2, 1]
print('插入排序:', insert_sort(lists))
print('冒泡排序:', bubble_sort(lists))
print('快速排序:', quick_sort(lists, 0, 4))
