# -*-coding:utf-8-*-
# ！usr/bin/env python
"""
Created on 2017年3月3日
二叉树的使用
@author: 武明辉
"""
from typing import List
from collections import deque


class BitNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    
class BiTree(object):
    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def build_bitree_from_list(lists: List[object]) -> object:
        if not lists:
            return None
        root_node = BitNode(lists[0])
        queue = deque([root])
        i = 1
        while i < len(lists):
            node = queue.popleft()
            node.left = BitNode(lists[i]) if lists[i] else None
            queue.append(node.left)
            i += 1
            node.right = BitNode(lists[i]) if lists[i] else None
            queue.append(node.right)
            i += 1
        return BiTree(root_node)

    def create_tree(self, root):
        data = input('请输入：')
        if not data:
            root.data = None
        else:
            root.data = data
            root.left = BitNode()
            self.create_tree(root.left)
            root.right = BitNode()
            self.create_tree(root.right)

    def pre_traverse(self, root):
        if root and root.data:
            print(root.data)
            self.pre_traverse(root.left)
            self.pre_traverse(root.right)

    def in_traverse(self, root):
        if root and root.data:
            self.in_traverse(root.left)
            print(root.data)
            self.in_traverse(root.right)

    def post_traverse(self, root):
        if root and root.data:
            self.post_traverse(root.left)
            self.post_traverse(root.right)
            print(root.data)

    def traverse_without_recursion(self):
        r = self.root
        s = []
        while r or s:
            while r:
                print(r.data)
                s.append(r)
                r = r.left
            if s:
                t = s.pop()
                r = t.right


if __name__ == '__main__':
    """
           A
          / \
         B   C
        / \  /
       D   E F
    """
    n1 = BitNode(data="D")
    n2 = BitNode(data="E")
    n3 = BitNode(data="F")
    n4 = BitNode(data="B", left=n1, right=n2)
    n5 = BitNode(data="C", left=n3, right=None)
    root = BitNode(data="A", left=n4, right=n5)
    tree = BiTree(root)
    # tree.create_tree(tree.root)
    print('先序遍历')
    tree.pre_traverse(root)
    print('中序遍历')
    tree.in_traverse(root)
    print('后续遍历')
    tree.post_traverse(root)
    print('非递归先序遍历')
    tree.traverse_without_recursion()
