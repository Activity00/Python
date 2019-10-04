"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_list(self, first, second):
        head = cur = ListNode(None)
        while first and second:
            if first.val < second.val:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next

        cur.next = first if first else second
        return head.next

    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        ret = None
        for li in lists:
            ret = self.merge_two_list(ret, li)
        return ret

    def merge_recursion(self, lists, p, r):
        if p == r:
            return lists[p]
        q = (p + r) // 2
        left = self.merge_recursion(lists, p, q)
        right = self.merge_recursion(lists, q + 1, r)
        return self.merge_two_list(left, right)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge_recursion(lists, 0, len(lists) - 1)


"""
看到题目, 想到以往的书中提到的，应该是可以用归并排序的思路解决问题。但是第一次写并没有用归并而是迭代
循环依次合并两个链表，这种方法执行时间5000多毫秒，17M内存显然不是很好。

第二次尝试就是归并排序思路了， 但是局限与归并排序，思路固化。在想到使用第一次的合并算法却没有将归并中的
返回列表转换成单个结点,这也是对递归式的不灵活运用。而且依旧对归并排序中除以2后的临界值作为擦参数把握不好

临界值： //2 操作本身是向下去整 所以//2 和 //2 + 1 以下标刚好分列表一分为二
转换列表到单个： 归并排序中在'if p < q:' 中原址排序, 递归操作不返回值，当需要值可以通过终止条件来返回.
本题目中递归式终止条件就是剩下一个的时候，不要去考虑merge的返回。得到终止条件再去考虑合并的返回结果
但是这种方法提交递归深度超了,sys.setrecursionlimit(1000000) 后一百多毫秒

最后查看网上答案, 最小堆，先排序，是很好理解和高效的方法。
"""