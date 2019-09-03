# coding: utf-8

"""
@author: 武明辉 
@time: 2018/7/5 11:03
"""
"""
     A --> B
     A --> C
     B --> C
     B --> D
     C --> D
     D --> C
     E --> F
     F --> C


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

"""


def find_path(graph, start, end, path=[]):
        """寻找一条路径"""
        path = path + [start]
        if start == end:
            return path
        if start not in range(len(graph)):
            return None
        for i, node in enumerate(graph[start]):
            if node == 1 and i not in path:
                new_path = find_path(graph, i, end, path)
                if new_path:
                    return new_path
        return path


def find_all_paths(graph, start, end, path=[]):
        """查找所有的路径"""
        path = path + [start]
        if start == end:
            return [path]
        if start not in range(len(graph)):
            return []
        paths = []
        for i, node in enumerate(graph[start]):
            if node == 1 and i not in path:
                newpaths = find_all_paths(graph, i, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


def find_shortest_path(graph, start, end, path=[]):
        """查找最短路径"""
        path = path + [start]
        if start == end:
            return path
        if start not in range(len(graph)):
            return None
        shortest = None
        for i, node in enumerate(graph[start]):
            if node == 1 and i not in path:
                newpath = find_shortest_path(graph, i, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


if __name__ == '__main__':
    graph = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0]
    ]
    #print(find_path(graph, 0, 3))
    print(find_all_paths(graph, 0, 3))
    #print(find_shortest_path(graph, 0, 3))
