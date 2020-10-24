# /usr/bin/env python

def  brackets_match(s):
    stack=[]
    dic={')':'(', ']':'[', '}':'{'}
    for i in s:
        if stack and i in dic:
            if stack[-1]==dic[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not stack

s='(){}[]{()}'
a=brackets_match(s)
print(a)
