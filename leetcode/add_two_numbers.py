# coding: utf-8

"""
@author: 武明辉 
@time: 18-10-30 上午11:49
"""
import doctest

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_list(self):
        ret = []
        n = self
        while n:
            ret.append(n.val)
            n = n.next
        return ret


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        >>> l1 = ListNode(2)
        >>> l1.next = ListNode(4)
        >>> l1.next.next = ListNode(3)
        >>> l2 = ListNode(5)
        >>> l2.next = ListNode(6)
        >>> l2.next.next = ListNode(4)
        >>> s = Solution()
        >>> ret = s.addTwoNumbers(l1, l2)
        >>> ret.get_list()
        [7, 0, 8]
        >>> l3 = ListNode(5)
        >>> l4 = ListNode(5)
        >>> ret = s.addTwoNumbers(l3, l4)
        >>> ret.get_list()
        [0, 1]
        >>> l7 = ListNode(9)
        >>> l7.next = ListNode(8)
        >>> l8 = ListNode(1)
        >>> ret = s.addTwoNumbers(l7, l8)
        >>> ret.get_list()
        [0, 9]
        """
        root = tmp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, b = divmod(carry, 10)
            tmp.next = ListNode(b)
            tmp = tmp.next
        return root.next


if __name__ == '__main__':
    doctest.testmod()
