"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverse_link(self, head):
        cur = head
        pre = None
        nxt = cur.next
        while nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = cur.next
        cur.next = pre
        return cur

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if head.next.next is None:
            return head.val == head.next.val

        fast = slow = q = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p = self.reverse_link1(slow.next)
        while p:
            if p.val != q.val:
                break
            p = p.next
            q = q.next
        else:
            return True
        return False
