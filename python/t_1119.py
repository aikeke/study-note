#/usr/bin/env python
def quick(a,s,e):
    if s<e:
        mid=part(a,s,e)
        quick(a,s,mid-1)
        quick(a,mid+1,e)

import os
file=[]
dir_name='/study-note'
def get_file(dir_name):
    for i in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name,i)):
            file.append(i)
        else:
            get_file(os.path.join(dir_name,i))
get_file(dir_name)
b=sorted(file)
print b
