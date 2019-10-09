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
"""
刚看到题目感觉就是成对反转的加强版，只要在那基础上迭代就可以完成。 而实际上真正去做的时候遇到问题1.想把逆转过程也写进循环去这导致了多个临时变量操作后混乱
2.当决定拆出逆转过程却看到链表一直链接到末尾而没有灵活转化3.总是绝的这个方法好陷入，把可以相对简单内存换时间的使用其他数据结构的思路忽略了。

看到现在这个答案就相对清晰了， 总的三个变量， 然后利用reverse反转链表
"""