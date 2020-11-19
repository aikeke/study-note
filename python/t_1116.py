import t_1112
def quick_sort(alist,start,end):
    if start<end:
        mid=part(alist,start,end)
        quick_sort(alist,start,mid-1)
        quick_sort(alist,mid+1,end)

def part(alist,start,end):
    done=False
    l=start+1
    r=end
    target=alist[start]
    while not done:
        if l<=r and alist[l]<=target:
            l+=1
        if l<=r and alist[r]>=target:
            r-=1
        if l<=r:
            alist[l],alist[r]=alist[r],alist[l]
        else:
            done=True
    alist[start],alist[r]=alist[r],alist[start]
    return r

def reconstructQueue(self, people):
    if len(people) <= 1:
        return people
    people = sorted(people, key = lambda x: (-x[0], x[1]))
    new_people = [people[0]]  
    for i in people[1:]:
        new_people.insert(i[1], i)
    return new_people

import threading
class mysql_obj(object):
    instance=None
    lock=threading.RLock()
    def __init__(self):
        pass

    def __new__(cls,*args,**kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                cls.instance=object.__new__(cls)
            return cls.instance

for i in range(10):
    print mysql_obj()


