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
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                new_path = find_path(graph, node, end, path)
                if new_path:
                    return new_path
        return path


def find_all_paths(graph, start, end, path=[]):
        """查找所有的路径"""
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


def find_shortest_path(graph, start, end, path=[]):
        """查找最短路径"""
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

    print(find_path(graph, 'A', 'D'))
    print(find_all_paths(graph, 'A', 'D'))
    print(find_shortest_path(graph, 'A', 'D'))
