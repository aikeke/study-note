#/usr/bin/env python
# -*- coding: utf-8 -*-
#python 实现 deque 双端队列

class Deque(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def addRear(self.item):
        self.items.peend(item)

    def addFront(self.item):
        self.items.insert(0,item)

    def size(self):
        return len(self.items)
    
    def removeRear(self):
        return self.items.pop()

    def removeFront(self):
        return self.items.pop(0)
