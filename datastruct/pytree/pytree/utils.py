from collections import deque


def print_space(num):
    for i in range(num):
        print(' ', end='')


def print_tree(tree):
    max_height = tree.height
    space_nums = [2 ** i - 1 for i in range(max_height)[::-1]]
    row = 0
    stack = deque([tree.root])
    while stack:
        flag = 0
        j = row
        tmp = []
        while stack:
            if flag >= 1:
                print_space(space_nums[j])
            else:
                print_space(space_nums[j])
                j -= 1
            flag += 1
            s = stack.popleft()
            if s:
                if s.data:
                    print(s.data, end='')
                tmp.append(s.left)
                tmp.append(s.right)
            else:
                tmp.append(None)
                tmp.append(None)
                print(' ', end='')
        stack.extend(tmp)
        row += 1
        if not any(stack):
            break
        print('\n')
    print('\n')


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

