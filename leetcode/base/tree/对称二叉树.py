# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-19 下午10:31
"""
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.symmetric(root.left, root.right)

    def symmetric(self, left, right):
        if not left and not right:
            return True
        if left and not right or right and not left:
            return False
        return left.val == right.val and self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        nodeList = [root.left, root.right]
        while nodeList:
            symmetricLeft = nodeList.pop(0)
            symmetricRight = nodeList.pop(0)
            if not symmetricLeft and not symmetricRight:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricLeft.val != symmetricRight.val:
                return False
            nodeList.append(symmetricLeft.left)
            nodeList.append(symmetricRight.right)
            nodeList.append(symmetricLeft.right)
            nodeList.append(symmetricRight.left)
        return True


if __name__ == '__main__':
    pass
