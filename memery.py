import numpy as np
import pandas as pd


def empricalEntropy(data, classes):
    # 计算每个类的样本数
    C = {}  # 记录每个类样本数的字典
    C_temp = data.groupby(by=[classes]).groups  # 记录每个类索引的字典
    for key in C_temp.keys():
        C[key] = len(C_temp[key])

    H_D = 0  # 初始化熵
    for key in C.keys():  # key取0，1
        H_D -= C[key] / len(data) * np.log2(C[key] / len(data))

    return H_D


def empricalConditionalEntropy(data, feature, classes):
    D_temp = data.groupby(by=[feature]).groups  # 返回统计特征A的数据字典，它的key是特征A的各个取值，value是索引
    C_temp = data.groupby(by=[classes]).groups  # 返回统计分类的字典，它的key是分类的各个取值，value是索引

    H_DA = 0  # 初始化条件熵
    for key, i_index in D_temp.items():  # D_temp的key是特征的各个取值
        D_i = len(i_index)  # 索引的长度，即为某个特征值的样本个数

        classConditionalEntropy = 0  # H初始化H(Y|X=x_i)
        for label, k_index in C_temp.items():  # key为0或者1
            D_ik = len(list(set(i_index).intersection(set(k_index))))  # set(A).intersection(B)取集合A和B的交集
            if D_ik == 0:  # 计算机会在计算log0时返回nan，所以要把0的情况单独处理
                classConditionalEntropy += 0
            else:
                classConditionalEntropy += (D_ik / D_i) * (np.log2(D_ik / D_i))

        D = len(data)
        H_DA -= D_i / D * classConditionalEntropy

    return H_DA


def infoGain(data, features, classes):
    H_D = empricalEntropy(data, classes)

    # 初始化
    maxEntropy = 0
    maxFeature = ''

    for feature in features:
        H_DA = empricalConditionalEntropy(data, feature, classes)

        G = H_D - H_DA

        print(feature, G)  # 输出各个特征和G，方便查看

        # 选出最优特征
        if G > maxEntropy:
            maxEntropy = G
            maxFeature = feature

    return maxEntropy, maxFeature


data = pd.read_excel('Coupon_Assignment2.xlsx')
label = data.columns
features = list(label[1: -1])
classes = label[-1]
c = data.groupby(by=[classes]).groups
H_D = empricalEntropy(data, classes)
H_DA = empricalConditionalEntropy('data')
