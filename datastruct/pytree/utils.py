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
