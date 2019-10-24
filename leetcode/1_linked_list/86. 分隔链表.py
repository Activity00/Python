"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition_first_error(self, head: ListNode, x: int) -> ListNode:
        first = ListNode(None)
        second = ListNode(None)
        first.next = head
        second.next = head
        first_end = None
        while second.next and second.next.val < x:
            first_end = second.next
            second.next = second.next.next

        second_end = second.next
        cur = second.next.next
        while cur:
            if cur.val < x:
                first_end.next = cur
                first_end = cur
            else:
                second_end.next = cur
                second_end = cur
            cur = cur.next
        first_end.next = second.next
        return first.next

    def partition_first_error(self, head: ListNode, x: int) -> ListNode:
        first = ListNode(None)
        second = ListNode(None)
        cur = head
        cur1 = first
        cur2 = second
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur = cur.next
                cur1 = cur1.next
                cur1.next = None
            else:
                cur2.next = cur
                cur = cur.next
                cur2 = cur2.next
                cur2.next = None

        cur1.next = second.next
        return first.next

"""
首先看到这个问题感觉问题不大， 但是却是因为没有考虑清楚. 如果第一个开始就大与x等问题。

看了答案感觉思路清晰但是操作起来还是遇到了问题1.新结点和结点的名字不是同一个概念。 eg: cur 只是一个名字不应该画指向箭头！！！ 还有最后没处理
结束而死循环。
"""