# coding: utf-8

"""
@author: 武明辉 
@time: 2018/6/26 8:53
"""
from sklearn import tree

if __name__ == '__main__':
    X = [[0, 0], [1, 1]]
    Y = ['xxx', 'ooo']
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    print(clf.predict([[2, 2]]))
    print(clf.predict_proba([[2., 2.]]))