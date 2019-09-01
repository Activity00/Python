from typing import Callable

from datastruct.pytree.pytree.tree import BiTree


def level_traversal(btree: BiTree, func: Callable) -> None:
    if btree is None:
        return
    queue = [btree]
    while queue:
        q = queue.pop(0)
        func(q)
        if q.left:
            queue.append(q.left)
        if q.right:
            queue.append(q.right)


def print_tree(btree: BiTree) -> None:
    """
    因为树越深，叶子越茂盛。为了保证打印出的结果不要太紧凑，底层叶子结点至少间隔一个位置
    所以计算树高 通过计算出底层叶子最大可能值可以确定每层的第一个结点前面的空格数， 当前行的
    第二个空行正好是前一行第一个值的空行数目
    最后通过层序遍历打印结果
    """
    if btree is None:
        return

    height = btree.height
    spaces = [2**i - 1 for i in range(height)[::-1]]
    row = 0
    queue = [btree]
    while queue:
        cur_queue = []
        while queue:
            cur_queue.append(queue.pop(0))
        j = row
        flag = True
        while cur_queue:
            q = cur_queue.pop(0)
            if flag:
                print(' ' * spaces[j], end='')
                flag = False
            else:
                print(' ' * spaces[j-1], end='')
            if q is None:
                print(' ', end='')
            else:
                print(q.data, end='')
                queue.append(q.left)
                queue.append(q.right)

        print('\n')
        row += 1
        if not any(queue):
            break


def in_order_traverse(node, func, is_ret=False):
    if not node:
        return
    ret = [] if is_ret else None
    tmp_node = node
    stack = []
    while tmp_node or stack:
        while tmp_node:
            stack.append(tmp_node)
            tmp_node = tmp_node.left
        if stack:
            n = stack.pop()
            if n:
                r = func(n)
                if is_ret:
                    ret.append(r)
            if n.right:
                tmp_node = n.right
    return ret


def _in_order_traverse(node, func):
    if node:
        _in_order_traverse(node.left, func)
        func(node)
        _in_order_traverse(node.right, func)


def pre_order_traverse(node, func, is_ret=False):
    if not node:
        return
    ret = [] if is_ret else None
    stack = [node]
    while stack:
        n = stack.pop()
        r = func(n)
        if is_ret:
            ret.append(r)
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
    return ret


def _pre_order_traverse(node, func):
    if node:
        func(node)
        _pre_order_traverse(node.left, func)
        _pre_order_traverse(node.right, func)


def post_order_traverse(node, func, is_ret=False):
    if not node:
        return
    ret = [] if is_ret else None
    stack1 = [node]
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
        r = func(n)
        if is_ret:
            ret.append(r)
    return ret


def _post_order_traverse(node, func):
    if node:
        _pre_order_traverse(node.left, func)
        _pre_order_traverse(node.right, func)
        func(node)

