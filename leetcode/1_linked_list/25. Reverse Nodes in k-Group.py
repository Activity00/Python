"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1, 2, 3, 4, 5


class Solution:
    def reverse(self, head: ListNode):
        cur = head
        pre = None
        while cur:
            nt = cur.next
            cur.next = pre
            pre = cur
            cur = nt
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tmp_head = ListNode(None)
        tmp_head.next = head
        pre = end = tmp_head
        while end.next:
            count = k
            while count > 0 and end:
                end = end.next
                count -= 1
            if end is None:
                break
            nt = end.next
            end.next = None
            start = pre.next
            pre.next = self.reverse(start)
            start.next = nt
            pre = start
            end = pre
        return tmp_head.next
