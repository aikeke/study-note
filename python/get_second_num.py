#!/usr/bin/env python
def get_second_num(l):
    first,second=max(l[0],l[1]),min(l[0],l[1])
    for i in l:
        if i > first:
            second=first
            first=i            
        elif i > second and i < first:
            second=i
        else:
            continue
    return second

if __name__=='__main__':
    l=[i for i in range(100)]
    num=get_second_num(l)
    print(num)
    
