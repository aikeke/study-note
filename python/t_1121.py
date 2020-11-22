#-*- coding:utf-8 -*-
#最长不重复子串
#/usr/bin/env python
def sloev():
    s=raw_input('string')
    alist=[]
    cur=0
    for i in s:
        if i not in alist:
            alist.insert(0,i)
        else:
            if len(alist)>cur:
                cur=len(alist)
            while True:
                temp=alist.pop()
                if temp == i:
                    break

#获取某路径下所有文件，并排序
import os
file_list=[]
dir_name='/var/lib/'

def get_file(dir_name):
    for file in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name,file)):
            file_list.append(file)
        else:
            get_file(os.path.join(dir_name,file))

get_file(dir_name)
file_list.sort()
print file_list
