# /usr/bin/python
# -*- coding: utf-8 -*-
# 总体来说，交换操作的处理时间大约是移动操作的3倍，因为后者只需进行一次赋值。在基准测试中，插入排序算法的性能很不错。

def quicksort(alist,start,end):
    if start < end:
        partion=part(alist,start,end)
        print partion
        quicksort(alist,start,partion-1)
        quicksort(alist,partion+1,end)

def part(alist,start,end):
    partion=alist[start]
    done=False
    l=start+1
    r=end
    while not done:
        while l<=r and alist[l]<=partion:
            l+=1
        while r>=l and alist[r]>=partion:
            r-=1
        if l>r:
            done=True
        else:
            alist[l],alist[r]=alist[r],alist[l]
    alist[start],alist[r]=alist[r],alist[start]
    return r

alist=[1,4,2,5,623,6,2,34]
quicksort(alist,0,len(alist)-1)
print alist
