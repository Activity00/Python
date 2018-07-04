"""
有一条河，河边有一个猎人牵着一头狼，一个男人带着两个小男孩，还有一个女人带着两个小女孩。
如果猎人离开，狼就会把所有人吃掉。
如果男人离开，女人会把两个小男孩掐死。
如果女人离开，男人会把两个小女孩掐死。
河里有一条船，船上只能乘坐两人（狼算一人），只有猎人、男人、女人会划船。
如何使他们全部过河？

看到这道题，首先想到的是农夫过河问题。既然这两个问题十分相似，那我就尝试按照农夫过河问题的思路，通过程序来找出该题的解。
"""


##########################################
# 问题：
# 有一条河，河边有一个猎人牵着一头狼，一个男人带着两个小男孩，还有一个女人带着两个小女孩
# 如果猎人离开，狼就会把所有人吃掉
# 如果男人离开，女人会把两个小男孩掐死
# 如果女人离开，男人会把两个小女孩掐死
# 河里有一条船，船上只能乘坐两人（狼算一人），只有猎人、男人、女人会划船
# 如何使他们全部过河？


##########################################
# 思路：
# 与农夫过河问题类似，参考 https://www.zhihu.com/question/29968331
# 一共有 8 个人（包含狼），每个人有两个状态：分别为在河的一侧，以及在河的另一侧
# 这两种状态可用一个二进制位表示，0 代表在河的一侧，1 代表在河的另一侧
# 则可用一个 8 位二进制数表示这 8 个人的状态，进行组合，一共有 256 个状态
# 通过坐船，可以使一种状态转变为另一种状态
# 如果状态从 00000000 转换到 11111111, 则说明所有人均到达河的另一侧 
# 将两种可以相互转变的状态相互连接，可以构建出一个用于表示状态转移情况的图
# 在图中找到一条从 00000000 到 11111111 的路径，即可解决该问题


PERSONS = ['男人', '男孩1', '男孩2', '女人', '女孩1', '女孩2', '猎人', '狼']


# dijkstra算法实现，有向图和路由的源点作为函数的输入，最短路径最为输出
def dijkstra(graph, src):
    if graph is None:
        return None
    # 定点集合
    nodes = [i for i in range(len(graph))]  # 获取顶点列表，用邻接矩阵存储图
    # 顶点是否被访问
    visited = list()
    visited.append(src)
    # 初始化dis
    dis = {src: 0}  # 源点到自身的距离为0
    for i in nodes:
        dis[i] = graph[src][i]
    path = {src: {src: []}}  # 记录源节点到每个节点的路径
    k = pre = src

    while nodes:
        temp_k = k
        mid_distance = float('inf')  # 设置中间距离无穷大
        for v in visited:
            for d in nodes:
                if graph[src][v] != float('inf') and graph[v][d] != float('inf'):  # 有边
                    new_distance = graph[src][v]+graph[v][d]
                    if new_distance <= mid_distance:
                        mid_distance = new_distance
                        graph[src][d] = new_distance  # 进行距离更新
                        k = d
                        pre = v
        if k != src and temp_k == k:
            break
        dis[k] = mid_distance  # 最短路径
        path[src][k] = [i for i in path[src][pre]]
        path[src][k].append(k)

        visited.append(k)
        nodes.remove(k)
        # print(nodes)
    return dis, path


# 判断是否为危险的状态
def is_dangerous(x):
    # 男人，男孩，男孩，女人，女孩，女孩，猎人,狼
    # 第一种不安全的情况：男人不在，女人在，男孩在
    if (x & 0b10000000) == 0 and (x & 0b00010000) != 0 and (x & 0b01100000) != 0:
        return True
    if (~x & 0b10000000) == 0 and (~x & 0b00010000) != 0 and (~x & 0b01100000) != 0:
        return True
    # 第二种不安全的情况：女人不在，男人在，女孩在
    if (x & 0b00010000) == 0 and (x & 0b10000000) != 0 and (x & 0b00001100) != 0:
        return True
    if (~x & 0b00010000) == 0 and (~x & 0b10000000) != 0 and (~x & 0b00001100) != 0:
        return True
    # 第三种不安全的情况：猎人不在，狼在，其他人在
    if (x & 0b00000010) == 0 and (x & 0b00000001) != 0 and (x & 0b11111100) != 0:
        return True
    if (~x & 0b00000010) == 0 and (~x & 0b00000001) != 0 and (~x & 0b11111100) != 0:
        return True
    return False


# 船允许的所有状态，1 代表在船上
# 将两个状态进行异或操作，发生变化的位就会置一，则说明置一的位所对应的人是在船上
# 但是，船的行驶是有方向的，例如从 10000000 到 01000000 的状态是无法通过一次乘船达到的
# 男人，男孩，男孩，女人，女孩，女孩，猎人,狼
boat_allowed_states = [
    0b11000000, 0b10100000, 0b00011000, 0b00010100, 0b10000010,
    0b01000010, 0b00100010, 0b00010010, 0b00001010, 0b00000110,
    0b00000011, 0b10010000, 0b10000000, 0b00010000, 0b00000010,
    0b10000000, 0b00010000, 0b00000010
]


def convert_to_person(ps):
    t = []
    for i, s in enumerate(ps):
        if s == '1':
            t.append(PERSONS[i])
    return ','.join(t)


def show_process(path):
    l = len(path)
    for i in range(1, l):
        tmp = path[i] ^ (path[i - 1])
        persons = convert_to_person('{0:08b}'.format(tmp))
        if i % 2 == 0:
            print(persons, '---回来')
        else:
            print(persons, '---过对岸')


def show_status(path):
    for p in path:
        persons = convert_to_person('{0:08b}'.format(p))
        print(persons)


def find_all_paths(graph, start, end):
    stack = list()
    visted = set()
    stack.append(stack)
    visted.add(start)
    while stack:
        v = stack[-1]
        for g in graph[v]:
            if 0 < g < float('inf') and g not in stack and g not in visted:
                stack.append(g)
            else:
                pass


if __name__ == '__main__':
    states_graph = [[float('inf')] * 256 for i in range(256)]  # 创建 256x256 二维数组
    for i in range(256):
        states_graph[i][i] = 0
    for i in range(256):
        if is_dangerous(i):
            continue
        for j in range(256):
            if is_dangerous(j):
                continue
            # 如果通过坐船，可以使状态 x 转变为状态 y, 则使矩阵对应位置为 1
            tmp = i ^ j
            if tmp in boat_allowed_states:
                # 进一步判断，排除类似 10000000 到 01000000 的情况
                # 都是本岸 or 都是对岸
                if tmp & i ^ tmp == 0 or tmp & i ^ tmp == tmp:
                    states_graph[i][j] = 1  # 连接图中能够能够转换的状态

    print(dfs())
    # distance, path = dijkstra(states_graph, 0)  # 查找从源点0开始到其他节点的最短路径
    # show_process(path[0][255])
    # print('*'*50)
    # show_status(path[0][255])
