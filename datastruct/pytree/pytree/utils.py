from typing import Callable, Union

from datastruct.pytree.pytree.tree import BSTree, BitNode, BiTree


def print_tree(btree: Union[BiTree, BSTree]) -> None:
    """
    因为树越深，叶子越茂盛。为了保证打印出的结果不要太紧凑，底层叶子结点至少间隔一个位置
    所以计算树高 通过计算出底层叶子最大可能值可以确定每层的第一个结点前面的空格数， 当前行的
    第二个空行正好是前一行第一个值的空行数目
    最后通过层序遍历打印结果
    """
    if btree is None:
        return
    str_space = ' '
    height = btree.height
    spaces = [2 ** (i+1) - 1 for i in range(height)[::-1]]
    row = 0
    queue = [btree.root]
    while any(queue):
        cur_queue = []
        while queue:
            cur_queue.append(queue.pop(0))

        flag = True
        while cur_queue:
            q = cur_queue.pop(0)
            if flag:
                print(str_space * spaces[row], end='')
                flag = False
            else:
                print(str_space * spaces[row - 1], end='')
            if q is None:
                print(str_space, end='')
            else:
                print(q.data, end='')
            queue.append(q.left if q else None)
            queue.append(q.right if q else None)

        print('\n')
        row += 1


def level_traversal(btree: BiTree, func: Callable) -> None:
    if btree is None:
        return
    queue = [btree.root]
    while queue:
        q = queue.pop(0)
        func(q)
        if q.left:
            queue.append(q.left)
        if q.right:
            queue.append(q.right)


def pre_order_traverse(btree: BiTree, func: Callable) -> None:
    if not btree:
        return

    stack = [btree.root]
    while stack:
        n = stack.pop()
        func(n)
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)


def in_order_traverse(btree: BiTree, func: Callable) -> None:
    if not btree:
        return
    tmp_node = btree.root
    stack = []
    while tmp_node or stack:
        while tmp_node:
            stack.append(tmp_node)
            tmp_node = tmp_node.left

        n = stack.pop()
        func(n)
        if n.right:
            tmp_node = n.right


def post_order_traverse(btree: BiTree, func: Callable) -> None:
    if not btree:
        return
    stack1 = [btree.root]
    stack2 = []
    while stack1:
        n = stack1.pop()
        if n.left:
            stack1.append(n.left)
        if n.right:
            stack1.append(n.right)
        stack2.append(n)
    while stack2:
        n = stack2.pop()
        func(n)
