#/usr/bin/env python
#python stack
class Stack(object):
    def __init__(self):
        self.items=[]
  
    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item) 

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items) 

def new_bin(num):
    s=Stack()
    while num >0:
        s.push(num%2)
        num=num//2
    res=''
    for i in range(s.size()):
        res+=str(s.pop())
    return res

res=new_bin(13)
print res
print bin(13)

