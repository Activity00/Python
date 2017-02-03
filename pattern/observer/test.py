#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月3日

@author: 武明辉
'''
from pattern.observer import Observer, Observerable


class Thief(Observer):
    def __init__(self):
        super(Thief,self).__init__()
class Police(Observer):
    def __init__(self):
        Observer.__init__(self) 
class Car(Observerable):
    def __init__(self):
        Observerable.__init__(self)
car=Car()
car.addObserver(Thief())
car.addObserver(Police())
car.noifyObservers()

