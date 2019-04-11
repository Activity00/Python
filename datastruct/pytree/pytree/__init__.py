# coding: utf-8

"""
@author: 武明辉
@time: 18-9-28 上午9:35
"""
from typing import List
from collections import deque

from datastruct.pytree.pytree.utils import print_space, print_tree, in_order_traverse


class BitNode(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f'BiteNode({self.data})'


class BiTree(BitNode):
    def __str__(self):
        return f'BSTree->root({self.data})'

    @property
    def height(self):
        return self._height_with_node(self)

    @property
    def width(self):
        return self._width(self)

    @staticmethod
    def build_bstree(lists: List[object]) -> (None, 'BitNode'):
        if not lists:
            return None
        tree_node = BitNode(lists[0])
        queue = deque([tree_node])
        i = 1
        while i < len(lists):
            node = queue.popleft()
            node.left = node.right = None
            if lists[i]:
                node.left = BitNode(lists[i])
                queue.append(node.left)
            if lists[i + 1: i + 2] and lists[i + 1]:
                node.right = BitNode(lists[i + 1])
                queue.append(node.right)
            i += 2
        return tree_node

    def height_with_node(self, node):
        return 5

    def _width(self):
        # TODO
        cur_width = 1
        max_width = 0
        q = [self.root]
        while q:
            n = cur_width
            for i in range(n):
                tmp = q.pop(0)
                cur_width -= 1
                if tmp.left:
                    q.append(tmp.left)
                    cur_width += 1
                if tmp.right:
                    q.append(tmp.right)
                    cur_width += 1
            if cur_width > max_width:
                max_width = cur_width
        return max_width


class BSTree(BitNode):
    def __str__(self):
        return f'BSTree->root({self.data})'

    @property
    def min_num(self):
        return self._min_num(self)

    @property
    def max_num(self):
        return self._max_num(self)

    @staticmethod
    def _min_num(node):
        n = node
        while n.left:
            n = n.left
        return n.data

    @staticmethod
    def _max_num(node):
        n = node
        while n.right:
            n = n.right
        return n.data

    def tree_search(self, key, start_node=None):
        node = start_node if start_node else self.root
        while node and node.data != key:
            node = node.left if node.data > key else node.right
        return node

    def tree_search_recursion(self, key):
        return self._tree_search_recursion(self.root, key)

    def _tree_search_recursion(self, node, key):
        if not node or node.data == key:
            return node
        if node.data > key:
            return self._tree_search_recursion(node.left, key)
        else:
            return self._tree_search_recursion(node.right, key)

    def _height_recursion(self, root):
        return 0 if not root else max(self._height_recursion(root.left), self._height_recursion(root.right)) + 1

    def tree_successor(self, node):
        x = node
        if x.right:
            return self.min_num(x.right)
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y.data if y else None

    def insert(self, z):
        r = self.root
        y = None
        while r and r.data != z.data:
            y = r
            r = r.left if r.data > z.data else r.right
        z.parent = y
        if not y:
            root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

    def delete(self, node):
        # TODO
        if not node.parent:
            self.root = None
        if not node.left:
            if not node.right:
                node.parent
            else:
                pass


if __name__ == '__main__':
    """
                   15
               /        \ 
             6           18
           /  \         /  \
          3    7       17   20
         / \    \
        2   4    13 
                /
               9
    """
    tree_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9, None]
    tree = BSTree.build_bstree(tree_list)
    # 打印二叉搜索树
    # print('打印二叉搜索树：')
    # print_tree(tree)
    # 中序遍历
    print('中序遍历二叉搜索树:')
    # in_order_traverse(tree, lambda x: print(x.data) if x.data else None)
    # 最大最小值,高度与宽度
    print('最大值', tree.max_num)
    print('最小值', tree.min_num)
    print('宽度', tree.width)
    print('高度', tree.height)
    # 搜索二叉树
    print('搜索二叉树：')
    ret = tree.tree_search(20)
    print(20, ret)
    ret = tree.tree_search(200)
    print(200, ret)

    # print('15后继节点', tree.tree_successor(root))
    # print('13后继节点', tree.tree_successor(n13))
    # print('高度', tree.height(root), '宽度', tree.width(root))
    # tree.print_tree(root)
    # print('\n')
    # tree.insert(BitNode(data=8))
    # tree.print_tree(root)
    #
    # tree = BSTree.build_bitree_from_list(['A', 'B', 'C', 'D', 'E', 'F', None])
    # tree.print_tree(tree.root)
