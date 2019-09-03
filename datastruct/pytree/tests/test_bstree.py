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
        self.assertEqual(BSTree.node_max_num(self.tree).data, min([num for num in test_tree_list if num]))

    def test_max_num(self):
        self.assertEqual(self.tree.max_num, max([num for num in test_tree_list if num]))
        self.assertEqual(BSTree.node_min_num(self.tree).data, max([num for num in test_tree_list if num]))

    def test_height(self):
        self.assertEqual(self.tree.height, tree_height)

    def test_successor(self):
        self.assertEqual(17, BSTree.successor(self.tree.root).data)
        self.assertEqual(15, BSTree.successor(self.tree.search(13)).data)

    def test_successor(self):
        self.assertEqual(6, BSTree.pre_successor(self.tree.root).data)
        self.assertEqual(9, BSTree.pre_successor(self.tree.search(13)).data)
        self.assertEqual(7, BSTree.pre_successor(self.tree.search(9)).data)
        self.assertEqual(15, BSTree.pre_successor(self.tree.search(17)).data)
        self.assertEqual(None, BSTree.pre_successor(self.tree.search(2)))

    def test_search(self):
        self.assertEqual(self.tree.search(7).data, 7)
        self.assertEqual(self.tree.search(3).data, 3)
        self.assertEqual(self.tree.search(999), None)


if __name__ == '__main__':
    unittest.main()
