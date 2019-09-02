import unittest

from datastruct.pytree.pytree import BiTree
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


class TestBiTree(unittest.TestCase):

    def setUp(self):
        self.tree = BiTree.build_from_list(test_tree_list)

    def test_height(self):
        self.assertEqual(self.tree.height, tree_height)


if __name__ == '__main__':
    unittest.main()
