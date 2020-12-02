#/usr/bin/python

def quick_sort(alist,start,end):
    if start<end:
        mid=part(alist,start,end)
        quick_sort(alist,start,mid-1)
        quick_sort(alist,mid+1,end)

def part(alist,start,end):
    target=alist[start]
    done=False
    l=start+1
    r=end
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

alist=[1,31,6,23,7,2,373,74,7,-3,234,2,6,3,67,36,3]
quick_sort(alist,0,len(alist)-1)
print alist
