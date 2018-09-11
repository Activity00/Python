# coding: utf-8

"""
@author: 武明辉 
@time: 18-9-11 上午9:36
"""
import array

if __name__ == '__main__':
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    print(numbers)
    memv = memoryview(numbers)
    print(memv)
    print(memv[0])
    memv_otc = memv.cast("B")
    print(memv_otc.tolist())
    memv_otc[5] = 4
    print(numbers)


