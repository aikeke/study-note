# /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
python 3.x中自带了concurrent.futures模块 python 2.7需要安装futures模块，使用命令pip install futures安装即可
'''
import time
import threading
from concurrent.futures import ThreadPoolExecutor
pool=ThreadPoolExecutor(10)

def exec_time(func):
    def inner(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print(end_time-start_time)
    return inner

def task(num):
    time.sleep(num)
    print(threading.currentThread().name)

@exec_time
def run():
    print(threading.currentThread().name)
    for i in range(10):
        pool.submit(task,i)
    print(threading.currentThread().name)
run()
