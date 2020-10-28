#/usr/bin/env python
#-*- coding: utf-8 -*-
import time
def say_hello(log_file):
    def new_func(func):
        def inner(*args,**kwargs):
            start_time=time.time()
            func(*args,**kwargs)
            end_time=time.time()
            print(end_time-start_time)
            print(log_file)
        return inner
    return new_func

@say_hello(log_file='wife')
def func(n):
    print(n)
    time.sleep(2)
    print('结束了')
func(5)
