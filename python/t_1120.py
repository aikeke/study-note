#/usr/env python
# -*- coding: utf-8 -*-

import threading
class Singleton(object):
    instance=None
    lock=threading.RLock()
    def __init__(self):
        pass
    
    def __new__(cls,*args,**kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                cls.instance=object.__new__(cls)
            return cls.instance

def heapify(alist,n,i):
    while True:
        maxpos=i
        if 2*i <=n and alist[i]<alist[2*i]:
            maxpos=2*i
        if 2*i+1<=n and alist[maxpos]<alist[i*2+1]:
            maxpos=2*i+1
        if maxpos==i:
            break
        alist[i],alist[maxpos]=alist[maxpos],alist[i]
        i=maxpos

a=[0,33,27,21,16,13,15,14,5,6,7,8,1,2,12]
account=len(a)-1
a[1]=a[account]
heapify(a,account-1,1)
print a
