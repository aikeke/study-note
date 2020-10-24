# /usr/bin/env python
# -*- coding: utf-8 -*-
import threading

def door():
    if not event.isSet():
        event.set()
    count=0
    while True:
        if not event.isSet():
            count+=1
            print('door is open! 通过{}人 '.format(count))
            event.set()

def employee(name):
    if event.isSet():
        print('door is close!please use card')
        print('{} use card'.format(name))
        event.clear()
    else:
        print('{} pass'.format(name))

if __name__=='__main__':
    event=threading.Event()
    Door=threading.Thread(target=door)
    Door.start()
    for i in ['aikeke','difa','alice']:
        em=threading.Thread(target=employee,args=(i,))
        em.start()
 
