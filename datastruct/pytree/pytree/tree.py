from typing import List

from datastruct.pytree.pytree import print_tree
from datastruct.pytree.pytree.utils import level_traversal


class BitNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f'BiteNode({self.data})'

    def __bool__(self):
        return self.data is not None


class BiTree(BitNode):
    @property
    def root(self):
        return self

    @property
    def height(self):
        return self._height_recursion(self.root)

    def _height_recursion(self, root):
        return 0 if not root else max(self._height_recursion(root.left), self._height_recursion(root.right)) + 1

    def __str__(self):
        return f'BiTree->root({self.data})'

    @classmethod
    def build_from_list(cls, lists: List):
        if not lists:
            return None

        tree = BiTree(lists[0])
        queue = [tree.root]
        i = 1
        while i < len(lists):
            node = queue.pop(0)
            if lists[i] is not None:
                node.left = BitNode(lists[i])
                queue.append(node.left)
            if i + 1 < len(lists) and lists[i + 1] is not None:
                node.right = BitNode(lists[i + 1])
                queue.append(node.right)
            i += 2

        return tree


if __name__ == '__main__':
    tree_list = [15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9, None]
    btree = BiTree.build_from_list(tree_list)
    print_tree(btree)
    level_traversal(btree)
