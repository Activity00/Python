import unittest

from datastruct.pytree.pytree.tree import BSTree

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


class TestBSTree(unittest.TestCase):

    def setUp(self):
        self.tree = BSTree.build_from_list(test_tree_list)

    def test_min_num(self):
        self.assertEqual(self.tree.min_num, min([num for num in test_tree_list if num]))
        self.assertEqual(BSTree.node_max_num(self.tree), min([num for num in test_tree_list if num]))

    def test_max_num(self):
        self.assertEqual(self.tree.max_num, max([num for num in test_tree_list if num]))
        self.assertEqual(BSTree.node_min_num(self.tree), max([num for num in test_tree_list if num]))

    def test_height(self):
        self.assertEqual(self.tree.height, tree_height)


if __name__ == '__main__':
    unittest.main()
