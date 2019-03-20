"""
合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = r = ListNode(0)
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val > p2.val:
                r.next = ListNode(p2.val)
                p2 = p2.next
            else:
                r.next = ListNode(p1.val)
                p1 = p1.next
            r = r.next
        if p1:
            r.next = p1
        else:
            r.next = p2
        return head.next
