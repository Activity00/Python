# coding: utf-8

"""
@author: 武明辉 
@time: 18-8-1 下午3:27
"""

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # divide and conque
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        count = len(lists) // 2
        left = self.mergeKLists(lists[:count])
        right = self.mergeKLists(lists[count:])
        return self.merge_two_lists(left, right)

    def merge_two_lists(self, left, right):
        head = p = ListNode(None)
        while left and right:
            if left.val < right.val:
                node = ListNode(left.val)
                p.next = node
                left = left.next
            else:
                node = ListNode(right.val)
                p.next = node
                right = right.next
            p = p.next
        if left:
            p.next = left
        if right:
            p.next = right
        return head.next

    @staticmethod
    def print_list_node(list_node):
        while list_node:
            print(list_node.val)
            list_node = list_node.next

    @staticmethod
    def create_list_node(_list):
        head = p = ListNode(None)
        while _list:
            p.next = ListNode(_list.pop(0))
            p = p.next
        return head.next

    def create_node_lists(self, _lists):
        return [self.create_list_node(_list) for _list in _lists]


if __name__ == '__main__':
    s = Solution()
    s.print_list_node(s.mergeKLists(s.create_node_lists([[1, 4, 5], [1, 3, 4], [2, 6]])))
