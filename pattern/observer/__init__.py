import threading

class Observer(object):
    def __init__(self):
        pass
    def update(self):
        pass

class Observerable(object):
    def __init__(self):
        self.changed=False
        self._list_observer=[]
        self.mu=threading.Lock()
    def addObserver(self,o):
        if o is None:
            raise Exception
        self.mu.acquire()
        if o not in self._list_observer:
            self._list_observer.append(o)
        self.mu.release()
    
    def deleteObserver(self,o):
        self._list_observer.remove(o)
        
    def noifyObservers(self):
        print __class__,'start'
        self.__notifyObservers(None);
    
    def __notifyObservers(self,args):
        list_tmp=self._list_observer
        self.mu.acquire()
        if not self.changed:
            pass
        else:
            self.clearnchanged()
        self.mu.release()
        for i in list_tmp:
            i.update()
      
    def __clearnchanged(self):
        self.mu.acquire()
        self.changed=True
        self.mu.release()