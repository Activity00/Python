"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

ollow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseListz(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            nt = cur.next
            cur.next = pre

            pre = cur
            cur = nt

        return pre

    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return ret

    def reverseListzz(self, head):
        if not head:
            return None
        pre = ListNode(0)
        cur = ListNode(0)
        pre.next, cur.next = None, head
        while cur.next:
            nt = cur.next.next
            cur.next.next = pre.next

            pre.next = cur.next
            cur.next = nt
        return pre.next


if __name__ == '__main__':
    pass
