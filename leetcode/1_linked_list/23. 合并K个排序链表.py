"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_list(self, first, second):
        head = cur = ListNode(None)
        while first and second:
            if first.val < second.val:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next

        cur.next = first if first else second
        return head.next

    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        ret = None
        for li in lists:
            ret = self.merge_two_list(ret, li)
        return ret

    def merge_recursion(self, lists, p, r):
        if p == r:
            return lists[p]
        q = (p + r) // 2
        left = self.merge_recursion(lists, p, q)
        right = self.merge_recursion(lists, q + 1, r)
        return self.merge_two_list(left, right)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge_recursion(lists, 0, len(lists) - 1)
