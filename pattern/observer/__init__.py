import threading

'''
观察者模式
'''


class Observer(object):
    """抽象观察者
      只要一个更新
    """

    def __init__(self):
        pass

    def update(self):
        pass


class Observerable(object):
    """被观察者"""

    def __init__(self):
        self.changed = False
        self._list_observer = []
        self.mu = threading.Lock()

    def addObserver(self, o):
        if o is None:
            raise Exception
        self.mu.acquire()
        if o not in self._list_observer:
            self._list_observer.append(o)
        self.mu.release()

    def deleteObserver(self, o):
        self._list_observer.remove(o)

    def noifyObservers(self):
        print
        'Observerable', 'start'
        self.__notifyObservers(None);

    def __notifyObservers(self, args):
        list_tmp = self._list_observer
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
        self.changed = True
        self.mu.release()


class Thief(Observer):
    def __init__(self):
        super(Thief, self).__init__()

    def update(self):
        print('Thief update')


class Police(Observer):
    def __init__(self):
        Observer.__init__(self)

    def update(self):
        print('Police update')


class Car(Observerable):
    def __init__(self):
        Observerable.__init__(self)


if __name__ == '__main__':
    car = Car()
    car.addObserver(Thief())
    car.addObserver(Police())
    car.noifyObservers()
