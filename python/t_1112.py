#quick sort
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
        while left<=right and  alist[left]<=mid:
            left+=1
        while alist[right]>=mid and left<=right:
            right-=1
        if left>right:
            done=True
        else:
            alist[left],alist[right]=alist[right],alist[left]
    alist[start],alist[right]=alist[right],alist[start]
    print right
    return right

#binary_search
def bin_search(alist,a):
    mid=(len(alist)-1)/2
    print mid
    start=0
    end=len(alist)-1
    while start <= end:
        if a == alist[mid]:
            return True
        if a > alist[mid]:
            start=mid+1
            mid=(start+end)/2
        else:
            end=mid-1
            mid=(start+end)/2
    return False

l=[1,3,5,7,9,2,4,6,8,10]



