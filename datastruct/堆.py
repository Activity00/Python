# coding: utf-8

"""
@author: 武明辉 
@time: 18-8-3 上午10:48
"""
import heapq

if __name__ == '__main__':
    heap = []  # creates an empty heap
    heapq.heappush(heap, 5)  # pushes a new item on the heap
    item = heapq.heappop(heap)  # pops the smallest item from the heap
    item = heap[0]  # smallest item on the heap without popping it
    heapq.heapify(x)  # transforms list into a heap, in-place, in linear time
    item = heapq.heapreplace(heap, item)  # pops and returns smallest item, and adds
    # new item; the heap size is unchanged
