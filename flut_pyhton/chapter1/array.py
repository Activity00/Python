# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-11 上午9:23
"""
from array import array
from random import random

"""
如果是纯数字,array效率要好于list, array接近于c语言中array
"""


if __name__ == '__main__':
    floats = array('d', (random() for i in range(10**7)))
    print(floats[-1])
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()
    floats2 = array('d')
    fp = open('floats.bin', 'rb')  # 比直接生成快70倍
    floats2.fromfile(fp, 10**7)
    fp.close()
    print(floats2[-1])
