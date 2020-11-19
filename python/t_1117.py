#/usr/bin/env python
# -*- coding: utf-8 -*-
def quick_sort(alist,start,end):
    if start < end:
        mid=part(alist,start,end)
        quick_sort(alist,start,mid-1)
        quick_sort(alist,mid+1,end)

def part(alist,start,end):
    l=start+1
    r=end
    target=alist[start]
    done=False
    while not done:
        if l<=r and alist[l]<=target:
            l+=1
        if l<=r and alist[r]>=target:
            r-=1
        if l>r:
            done=True
        else:
            alist[l],alist[r]=alist[r],alist[l]
    alist[start],alist[r]=alist[r],alist[start]
    return r

l=[1,3,5,7,9,2,4,6,8,0]
quick_sort(l,0,9)

import threading
class sington(object):
    instance=None
    Lock=threading.RLock()
    def __init__(self):
        pass
    
    def __new__(cls,*args,**kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                cls.instance=object.__new__(cls)
            return cls.instance
#463
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        ans=0
        right,left=0,0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if j+1<n:
                    if grid[i][j]==1 and grid[i][j+1]==1:
                        right=2
                    else:
                        right=0
                else:
                    right=0
                if i+1<m:
                    if grid[i][j]==1 and grid[i+1][j]==1:
                        left=2
                    else:
                        left=0
                else:
                    left=0
                if grid[i][j]==1:
                    ans=ans+4-left-right
        return ans

