#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from concurrent import T

import time
from os import path
from queue import Queue
from threading import Thread


class ThreadBrute(Thread):
    """ Bruteforcer """
    get = "GET"

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            try:
                # if self.queue.full() == False: exit()
                if self.queue.empty():
                    break
                print(queue.maxsize)
                time.sleep(2)
                self.queue.task_done()
            except Exception as e:
                pass


queue = Queue([1, 2, 3, 4, 5])
threads = []
if __name__ == '__main__':
    for i in range(5):
        thread = ThreadBrute(queue)
        thread.daemon = False
        thread.start()
        thread.join()
