"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not k:
            return head
        ret_head, end = ListNode(None), ListNode(None)
        ret_head.next = end.next = head
        count = 1
        while end.next.next:
            end.next = end.next.next
            count += 1

        end.next.next = head
        step = count - k % count

        for _ in range(step):
            ret_head.next = ret_head.next.next
            end.next = end.next.next
        end.next.next = None
        return ret_head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    x = Solution().rotateRight(head, 2)

"""
拿到这个题目，第一印象还是比较容易的。 两个链表首位相接然后取余数循环就好然后尾结点下一个置空。 
然后第一个问题就是没有找对步数，因为是向右应该用总长-step。 第二个大问题就是竟然首尾两个结点指向了一个结点导致问题只纠结逻辑，没很快定位。

看其他答案，把问题直接转换到快慢指针移动。 感觉问题的转换好坏直接影响到了解决问题的效率。
"""