# coding: utf-8

"""
@author: 武明辉 
@time: 18-11-1 下午7:27
"""
import threading
import time


def count_down(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


if __name__ == '__main__':
    t = threading.Thread(target=count_down, args=(10, ), daemon=True)
    t.start()

    if t.is_alive():
        print('...')
    t.join()
    print('xxx')
