class Solution:
    def sortString(self, s):
        new_s=sorted(s)
        a=new_s[0]
        new_s.pop(0)
        while len(new_s)>0:
            i=0
            while i<len(new_s):
                if a[-1]<new_s[i]:
                    a=a+new_s[i]
                    new_s.pop(i)
                else:
                    i+=1
            if len(new_s)>0:
                a+=new_s[-1]
                new_s.pop()  
            i=len(new_s)-1                
            while i>=0 and len(new_s)>0:
                if a[-1]>new_s[i]:
                    a=a+new_s[i]
                    new_s.pop(i)
                else:
                    i-=1           
        return a

a=Solution()
s='aaaabbbbcccc'
print a.sortString(s)

