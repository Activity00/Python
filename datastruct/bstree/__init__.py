# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-28 上午9:35
"""
from typing import List
from collections import deque


"""
*                      1

 *
* *                    3 


   *    
 *   *   
* * * *               7

       *
   *       *
 *   *   *   *
* * * * * * * *      15       

"""


class BitNode(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f'BiteNode({self.data})'


class BSTree(object):
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return f'BSTree->root({self.root.val})'

    @staticmethod
    def build_bstree(lists: List[object]) -> 'BSTree':
        if not lists:
            return None
        root_node = BitNode(lists[0])
        queue = deque([root_node])
        i = 1
        while i < len(lists):
            node = queue.popleft()
            node.left = node.right = None
            if lists[i]:
                node.left = BitNode(lists[i])
                queue.append(node.left)
            if lists[i + 1: i + 2]:
                node.right = BitNode(lists[i + 1])
                queue.append(node.right)
            i += 2

        return BSTree(root_node)

    def _in_order_traverse(self, node, func):
        if node:
            self._in_order_traverse(node.left, func)
            func(node)
            self._in_order_traverse(node.right, func)

    def in_order_traverse(self, func):
        if not self.root:
            return
        node = self.root
        stack = deque()
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                n = stack.pop()
                if n:
                    func(n)
                    stack.append(n.right)

    def _in_order_traverse_recursion(self, func):
        self._in_order_traverse(self.root, func)

    @staticmethod
    def _print_space(num):
        for i in range(num):
            print(' ', end='')

    def print_tree(self):
        max_height = self.height
        space_nums = [2**i-1 for i in range(max_height)[::-1]]
        row = 0
        stack = deque([self.root])
        while stack:
            flag = 0
            j = row
            tmp = []
            while stack:
                if flag >= 1:
                    self._print_space(space_nums[j])
                else:
                    self._print_space(space_nums[j])
                    j -= 1
                flag += 1
                s = stack.popleft()
                if s:
                    if s.data:
                        print(s.data, end='')
                    tmp.append(s.left)
                    tmp.append(s.right)
                else:
                    tmp.append(None)
                    tmp.append(None)
                    print(' ', end='')
            stack.extend(tmp)
            row += 1
            if not any(stack):
                break
            print('\n')
        print('\n')

    def min_num(self):
        r = self.root
        while r.left:
            r = r.left
        return r.data

    def max_num(self):
        r = self.root
        while r.right:
            r = r.right
        return r.data

    def _height(self, root):
        if not root:
            return 0
        ld = self._height(root.left)
        rd = self._height(root.right)
        return ld + 1 if ld > rd else rd + 1

    @property
    def height(self):
        return self._height(self.root)

    @property
    def width(self):
        curwidth = 1
        maxwidth = 0
        q = [self.root]
        while q:
            n = curwidth
            for i in range(n):
                tmp = q.pop(0)
                curwidth -= 1
                if tmp.left:
                    q.append(tmp.left)
                    curwidth += 1
                if tmp.right:
                    q.append(tmp.right)
                    curwidth += 1
            if curwidth > maxwidth:
                maxwidth = curwidth
        return maxwidth

    def tree_search(self, root, key):
        if not root or root.data == key:
            return root

        if root.data > key:
            return self.tree_search(root.left, key)
        else:
            return self.tree_search(root.right, key)

    def tree_search_without_recursion(self, key):
        r = self.root
        while r and r.data != key:
            r = r.left if r.data > key else r.right
        return r

    def tree_successor(self, node):
        """
        求后继节点
        :param x:
        :return:
        """
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
    tree = BSTree.build_bstree(
        [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9, None]
    )
    # 中序遍历
    tree.print_tree()
    tree.in_order_traverse(lambda x: print(x.data) if x.data else None)
    # 搜索二叉树
    # print('递归搜索二叉树')
    # ret = tree.tree_search(root, 20)
    # print(ret, ret.data if ret else None)
    # ret = tree.tree_search(root, 200)
    # print(ret, ret.data if ret else None)
    # print('非递归调用')
    # ret = tree.tree_search_without_recursion(20)
    # print(ret, ret.data if ret else None)
    # ret = tree.tree_search_without_recursion(200)
    # print(ret, ret.data if ret else None)
    # print('最大值', tree.max_num(root))
    # print('最小值', tree.min_num(root))
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
