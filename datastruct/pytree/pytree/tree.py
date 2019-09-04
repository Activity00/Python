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


class BiTree:
    def __init__(self, root: BitNode):
        self.root = root

    @property
    def height(self):
        return self._height_recursion(self.root)

    def _height_recursion(self, root):
        return 0 if not root else max(self._height_recursion(root.left), self._height_recursion(root.right)) + 1

    @property
    def width(self):
        # TODO
        cur_width = 1
        max_width = 0
        q = [self.root]
        while q:
            n = cur_width
            for i in range(n):
                tmp = q.pop(0)
                cur_width -= 1
                if tmp.left:
                    q.append(tmp.left)
                    cur_width += 1
                if tmp.right:
                    q.append(tmp.right)
                    cur_width += 1
            if cur_width > max_width:
                max_width = cur_width
        return max_width

    def __str__(self):
        return f'BiTree->root({self.root})'

    @classmethod
    def build_from_list(cls, lists: List[object]) -> Union['BSTree', 'BiTree', None]:
        if not lists:
            return None

        root = BitNode(lists[0])
        queue = [root]
        i = 1
        while i < len(lists):
            node = queue.pop(0)
            if lists[i] is not None and node:
                node.left = BitNode(lists[i], parent=node)
                queue.append(node.left)
            else:
                queue.append(None)
            if i + 1 < len(lists) and lists[i + 1] is not None and node:
                node.right = BitNode(lists[i + 1], parent=node)
                queue.append(node.right)
            else:
                queue.append(None)
            i += 2

        return cls(root)


class BSTree(BiTree):

    # TODO build bstree from unsorted list
    @classmethod
    def build_from_list(cls, lists: List[int]):
        return super().build_from_list(lists)

    @property
    def min_num(self):
        node = self.root
        while node.left:
            node = node.left
        return node.data

    @property
    def max_num(self):
        node = self.root
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

    @staticmethod
    def pre_successor(node: BitNode) -> BitNode:
        x = node
        if x.left:
            return x.left

        y = x.parent
        while y and x == y.left:
            x = y
            y = y.parent
        return y

    def insert(self, node: BitNode) -> None:
        x = self.root
        y = x
        while x:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y.data < node.data:
            y.right = node
        else:
            y.left = node

    def transplant(self, u: BitNode, v: BitNode) -> None:
        """
        use v replace u
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def delete(self, z: BitNode):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = BSTree.node_min_num(z.right)
            if y.parent is not z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def __str__(self):
        return f'BSTree->root({self.root})'
