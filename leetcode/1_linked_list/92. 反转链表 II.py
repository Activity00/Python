"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummpy = ListNode(None)
        dummpy.next = cur = head
        pre = dummpy
        i = 1
        while i < m:
            pre = cur
            cur = cur.next
            i += 1

        thead = cur
        tpre = None
        nt = None
        while cur and i <= n:
            nt = cur.next
            cur.next = tpre
            tpre = cur
            cur = nt
            i += 1
        else:
            pre.next = tpre
            thead.next = cur

        return dummpy.next
