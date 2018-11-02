# coding: utf-8

"""
@author: 武明辉 
@time: 18-11-1 下午7:38
"""
import threading
import time


class CountdownTask:
    def __init__(self):
        self.is_running = True

    def terminated(self):
        self.is_running = False

    def run(self, n):
        while self.is_running and n > 0:
            n -= 1
            print('T-time', n)
            time.sleep(1)


if __name__ == '__main__':
    c = CountdownTask()
    threading.Thread(target=c.run, args=(10, ))
