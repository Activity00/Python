# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/25 9:14
"""
from sklearn.neighbors import NearestNeighbors

if __name__ == '__main__':
    x = [
        [-1,-1],
        [-2,-1],
        [-3,-2],
        [1,1],
        [2,1],
        [3,2],
    ]
    nb = NearestNeighbors().fit(x)
    print(nb.kneighbors_graph(x).toarray())
