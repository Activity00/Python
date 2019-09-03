from typing import List, Union


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
                node.left = BitNode(lists[i], parent=node)
                queue.append(node.left)
            if i + 1 < len(lists) and lists[i + 1] is not None:
                node.right = BitNode(lists[i + 1], parent=node)
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

    @staticmethod
    def node_max_num(node: BitNode):
        tmp_node = node
        while tmp_node.left:
            tmp_node = tmp_node.left
        return tmp_node

    def search(self, key: int) -> Union[None, BitNode]:
        return BSTree.tree_search(self.root, key)

    @staticmethod
    def tree_search(node: BitNode, key: int, ) -> Union[None, BitNode]:
        tmp_node = node
        while tmp_node:
            if tmp_node.data == key:
                return tmp_node
            tmp_node = tmp_node.left if tmp_node.data > key else tmp_node.right
        else:
            return None

    @staticmethod
    def node_min_num(node: BitNode) -> BitNode:
        tmp_node = node
        while tmp_node.right:
            tmp_node = tmp_node.right
        return tmp_node

    @staticmethod
    def successor(node: BitNode) -> BitNode:
        x = node
        if x.right:
            return BSTree.node_max_num(x.right)

        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def __str__(self):
        return f'BSTree->root({self.data})'
