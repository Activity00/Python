# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/24 15:37
"""
import doctest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_nums(l1, l2):
    """
    >>> l1 = ListNode(2)
    >>> l1.next = ListNode(4)
    >>> l1.next.next = ListNode(3)
    >>> l2 = ListNode(5)
    >>> l2.next = ListNode(6)
    >>> l2.next.next = ListNode(4)
    >>> add_two_nums(l1, l2)
    >>> l1 = ListNode(5)
    >>> l2 = ListNode(5)
    >>> add_two_nums(l1, l2)
    """
    root = p = ListNode(None)
    carry = 0
    ll1, ll2 = l1, l2
    while ll1 or ll2 or carry:
        carry, ret = divmod((ll1.val if ll1 else 0) + (ll2.val if ll2 else 0) + carry, 10)
        p.next = ListNode(ret)
        p = p.next
        ll1 = ll1.next if ll1 else None
        ll2 = ll2.next if ll2 else None
    return root.next


if __name__ == '__main__':
    doctest.testmod()