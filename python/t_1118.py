#/usr/bin/env python

def quick_sort(alist,start,end):
    if start<end:
        mid=part(alist,start,end)
        quick_sort(alist,start,mid-1)
        quick_sort(alist,mid+1,end)

def part(l,start,end):
    tar=l[start]
    left=start+1
    r=end
    done=False
    while not done:
        if left<=r and l[left]<=tar:
            left+=1
        if left<=r and l[r]>=tar:
            r-=1
        if left>r:
            done=True
        else:
            l[left],l[r]=l[r],l[left]
    l[start],l[r]=l[r],l[start]
    return r

class Solution:
    def canCompleteCircuit(self,gas,cost):
        length=len(gas)
        d=[]
        l=[]
        for i in range(length):
            l.append(gas[i]-cost[i])
            if gas[i]-cost[i]>=0:
                d.append(i)
        
        l=l*2
       
        sum=0
        for key in d:
            flag=True
            for i in range(key,key+length):
                sum+=l[i]
                if sum <0:
                    flag=False
                    sum=0
                    break
            if flag:
                return key
        return -1
gas=[5,1,2,3,4]
cost=[4,4,1,5,1]
a=Solution()
print a.canCompleteCircuit(gas,cost)
