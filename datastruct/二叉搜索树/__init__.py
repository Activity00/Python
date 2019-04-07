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
    def build_bitree_from_list(lists: List[object]) -> object:
        if not lists:
            return None
        root_node = BitNode(lists[0])
        queue = deque([root_node])
        i = 1
        while i < len(lists):
            node = queue.popleft()
            node.left = BitNode(lists[i]) if lists[i] else None
            queue.append(node.left)
            i += 1
            node.right = BitNode(lists[i]) if lists[i] else None
            queue.append(node.right)
            i += 1
        return BSTree(root_node)

    def in_order_walk(self, root):
        if root:
            self.in_order_walk(root.left)
            print(root.data)
            self.in_order_walk(root.right)

    def min_num(self, root):
        r = root
        while r.left:
            r = r.left
        return r.data

    def max_num(self, root):
        r = root
        while r.right:
            r = r.right
        return r.data

    def height(self, root):
        if not root:
            return 0
        ld = self.height(root.left)
        rd = self.height(root.right)
        return ld + 1 if ld > rd else rd + 1

    def width(self, root):
        curwidth = 1
        maxwidth = 0
        q = [root]
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

    def tree_search_without_recursion(self, root, key):
        r = root
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

    def insert(self, root, z):
        r = root
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

    def _print_space(self, num):
        for i in range(num):
            print(' ', end='')

    def print_tree(self, root):
        max_height = self.height(root)
        space_nums = [2**i-1 for i in range(max_height)[::-1]]
        row = 0
        stack = [root]
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
                s = stack.pop(0)
                if s:
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

    def delete(self, root, node):
        if not node.parent:
            root = None
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
    n15, n6, n18, n3, n7, n17, n20, n2, n4, n13, n9 = BitNode(data=15), BitNode(data=6), BitNode(data=18), \
                                                      BitNode(data=3), BitNode(data=7), BitNode(data=17), \
                                                      BitNode(data=20), BitNode(data=2), BitNode(data=4), \
                                                      BitNode(data=13), BitNode(data=9)
    n15.left, n15.right = n6, n18
    n6.left, n6.right, n6.parent = n3, n7, n15
    n18.left, n18.right, n18.parent = n17, n20, n15
    n3.left, n3.right, n3.parent = n2, n4, n6
    n7.left, n7.right, n7.parent = None, n13, n6
    n17.left, n17.right, n17.parent = None, None, n18
    n20.left, n20.right, n20.parent = None, None, n18
    n2.left, n2.right, n2.parent = None, None, n3
    n4.left, n4.right, n4.parent = None, None, n3
    n13.left, n13.right, n13.parent = n9, None, n7
    root = n15
    tree = BiTree(n15)
    # 中序遍历
    tree.in_order_walk(root)
    # 搜索二叉树
    print('递归搜索二叉树')
    ret = tree.tree_search(root, 20)
    print(ret, ret.data if ret else None)
    ret = tree.tree_search(root, 200)
    print(ret, ret.data if ret else None)
    print('非递归调用')
    ret = tree.tree_search_without_recursion(root, 20)
    print(ret, ret.data if ret else None)
    ret = tree.tree_search_without_recursion(root, 200)
    print(ret, ret.data if ret else None)
    print('最大值', tree.max_num(root))
    print('最小值', tree.min_num(root))
    print('15后继节点', tree.tree_successor(root))
    print('13后继节点', tree.tree_successor(n13))
    print('高度', tree.height(root), '宽度', tree.width(root))
    tree.print_tree(root)
    print('\n')
    tree.insert(root, BitNode(data=8))
    tree.print_tree(root)

    tree = BSTree.build_bitree_from_list(['A', 'B', 'C', 'D', 'E', 'F', None])
    tree.print_tree(tree.root)
