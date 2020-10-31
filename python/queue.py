#/usr/bin/env python
# -*- coding: utf-8 -*-
#python 实现队列

class Queue(object):
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)	

#传土豆
def hotPotato(namelist,num):
    Q=Queue()
    for item in namelist:
        Q.enqueue(item)
    while Q.size() >1:
        for i in range(num):
            Q.enqueue(Q.dequeue())
        Q.dequeue()
    return Q.dequeue()

print(hotPotato([1,2,3,4,5,6,7],2))
