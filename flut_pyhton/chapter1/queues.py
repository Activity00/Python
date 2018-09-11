# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-11 上午10:00
"""
from collections import deque

"""
list 模拟的队列先进先出pop(0)操作移动整个数组性能不及deque
deque 是线程安全的双端队列
"""
if __name__ == '__main__':
    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11,22,33])
    print(dq)
    dq.extendleft([10,20])
