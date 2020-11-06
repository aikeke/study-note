# /usr/bin/env python
# -*- coding: utf-8 -*-
# 短冒泡
def shortbubblesort(alist):
    exchange=True
    passnum=len(alist)-1
    while exchange and passnum>0:
        exchange=False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                exchange=True
        passnum-=1

a=[1,4,2,5,6,6,37,3]
shortbubblesort(a)
print a
