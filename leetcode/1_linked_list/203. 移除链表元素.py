"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummpy = ListNode(None)
        dummpy.next = head
        pre = dummpy
        cur = head
        while cur:
            nt = cur.next
            if cur.val == val:
                pre.next = nt
            else:
                pre = cur
            cur = nt
        return dummpy.next
