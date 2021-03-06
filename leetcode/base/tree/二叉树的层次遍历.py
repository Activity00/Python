# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-19 下午10:13
"""
from typing import List

"""给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        q = [root]

        while q:
            t_list = []
            for _ in range(len(q)):
                t = q.pop(0)
                t_list.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            if t_list:
                ret.append(t_list)
        return ret


if __name__ == '__main__':
    pass
