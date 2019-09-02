from typing import List


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
    def build_from_list(cls, lists: List[object]):
        if not lists:
            return None

        tree = cls(lists[0])
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


class BSTree(BiTree):

    # TODO build bstree from unsorted list
    @classmethod
    def build_from_list(cls, lists: List[int]):
        return super().build_from_list(lists)

    @property
    def min_num(self):
        node = self
        while node.left:
            node = node.left
        return node.data

    @property
    def max_num(self):
        node = self
        while node.right:
            node = node.right
        return node.data

