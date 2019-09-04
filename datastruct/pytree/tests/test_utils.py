import unittest

from datastruct.pytree.pytree import BiTree
from datastruct.pytree.pytree.utils import pre_order_traverse, post_order_traverse, in_order_traverse, level_traversal, \
    print_tree

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
test_tree_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, None, None, 9, None]

level_traverse_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
in_order_list = [2, 3, 4, 6, 7, 9, 13, 15, 17, 18, 20]
pre_order_list = [15, 6, 3, 2, 4, 7, 13, 9, 18, 17, 20]
post_order_list = [2, 4, 3, 9, 13, 7, 6, 17, 20, 18, 15]


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.tree = BiTree.build_from_list(test_tree_list)

    def test_level_traverse(self):
        ret = []
        level_traversal(self.tree, lambda x: ret.append(x.data))
        self.assertListEqual(ret, level_traverse_list)

    def test_in_order_traverse(self):
        ret = []
        in_order_traverse(self.tree, lambda x: ret.append(x.data))
        self.assertListEqual(ret, in_order_list)

    def test_pre_order_traverse(self):
        ret = []
        pre_order_traverse(self.tree, lambda x: ret.append(x.data))
        self.assertListEqual(ret, pre_order_list)

    def test_post_order_traverse(self):
        ret = []
        post_order_traverse(self.tree, lambda x: ret.append(x.data))
        self.assertListEqual(ret, post_order_list)

    def test_print_tree(self):
        print_tree(self.tree)


if __name__ == '__main__':
    unittest.main()
