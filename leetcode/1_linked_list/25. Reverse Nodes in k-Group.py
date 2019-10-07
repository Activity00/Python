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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tmp_head = ListNode(None)
        cur = group_head = head
        pre = None
        flag = True
        while cur:
            for _ in range(k):
                if cur is None:
                    break
                cur = cur.next
            else:
                group_cur = group_head
                group_next = None
                for _ in range(k):
                    group_next = group_cur.next
                    group_cur.next = pre
                    pre = group_cur
                    group_cur = group_next

                if flag:
                    tmp_head.next = group_cur
                    flag = False

                pre = group_head
                group_head = group_next
                continue

            pre.next = group_head
        return tmp_head.next

