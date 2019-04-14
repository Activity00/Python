import unittest

from datastruct.pytree.pytree import BSTree, in_order_traverse
from datastruct.pytree.pytree.utils import pre_order_traverse, post_order_traverse

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
test_tree_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9, None]
tree_height = 5
in_order_list = [2, 3, 4, 6, 7, 9, 13, 15, 17, 18, 20]
pre_order_list = [15, 6, 3, 2, 4, 7, 13, 9, 18, 17, 20]
post_order_list = [2, 4, 3, 9, 13, 7, 6, 17, 20, 18, 15]


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.tree = BSTree.build_bstree(test_tree_list)

    def test_in_order_traverse(self):
        ret = in_order_traverse(self.tree, lambda x: x.data if x else None, is_ret=True)
        self.assertListEqual(ret, in_order_list)

    def test_pre_order_traverse(self):
        ret = pre_order_traverse(self.tree, lambda x: x.data if x else None, is_ret=True)
        self.assertListEqual(ret, pre_order_list)

    def test_post_order_traverse(self):
        ret = post_order_traverse(self.tree, lambda x: x.data if x else None, is_ret=True)
        self.assertListEqual(ret, post_order_list)


if __name__ == '__main__':
    unittest.main()
