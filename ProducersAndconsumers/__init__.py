
import random
from threading import Thread, Lock
import time

__all__=['Produces','Consume']

queue=[]
lock=Lock()

class Produces(Thread):
    def run(self):
        nums=range(5)
        global queue
        while True:
            num=random.choice(nums)
            lock.acquire()
            queue.append(num)
            print 'Produced',num
            lock.release()
            time.sleep(random.random())
            
class Consumer(Thread):
    def run(self):
        global queue
        while True:
            lock.acquire()
            if not queue:
                print 'Nothing in queue but consume ttryto consume'
            num=queue.pop(0)
            print 'Consume',num
            lock.release()
            time.sleep(random.random())
        

Produces().start()
Consumer().start()
