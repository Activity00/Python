"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur and cur.next:
            first, second, third = cur, cur.next, cur.next.next
            second.next = first
            first.next = third

            if pre is None:
                head = second
            else:
                pre.next = second

            pre = first
            cur = third
        return head

    def swapPairsr(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second
