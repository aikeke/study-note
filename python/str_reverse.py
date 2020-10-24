# /usr/bin/python

def reverseString(s):
    #s.reverse()
    #s[:]=s[::-1]
    start,end=0,-1
    while start < int(len(s)/2):
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    
s=[i for i in 'hello']
reverseString(s)
print(s)
