# /usr/bin/python

def bubble_sort(List):
    l=len(List)
    for j in range(l):
        for i in range(l-j-1):
            if List[i]>List[i+1]:
                List[i],List[i+1]=List[i+1],List[i]
    print List

def insert_sort(L):
    l=len(L)
    for i in range(1,l):
        for j in range(i-1,-1,-1):
            if L[i]<L[j]:
                L[j+1]=L[j]
                
            else:
                break
         
        L[j+1]=L[i]
    print L

l=[1,2,4,5,2,56,2,3,7,8]
bubble_sort(l)
insert_sort(l)
