def quick_sort(alist,start,end):
    if start < end:
        mid=part(alist,start,end)
        quick_sort(alist,start,mid-1)
        quick_sort(alist,mid+1,end)

def part(alist,start,end):
    mid=alist[start]
    left=start+1
    right=end
    done=False
    while not done:
        if left<=right and alist[left]<=mid:
            left+=1
        if left<=right and alist[right]>=mid:
            right-=1
        if left>right:
            done=True
        else:
            alist[left],alist[right]=alist[right],alist[left]
    alist[start],alist[right]=alist[right],alist[start]
    return right

l=[1,3,5,7,9,2,4,6,8,10]
quick_sort(l,0,9)
print l

def binary_search(alist,n):
    start=0
    end=len(alist)-1
    mid=(start+end)/2
    while start<=end:
        if alist[mid]<=n:
            start=mid+1
            mid=(start+end)/2
        else:
            if mid==0 or alist[mid-1]<=n:
                return alist[mid]
            else:
                end=mid-1
                mid=(start+end)/2
    return None
l=[1,2,3,4,5,6]
print binary_search(l,1)
