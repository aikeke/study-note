class Solution:
    def minRemoveToMakeValid(self, s):
        stack=[]
        flag=0
        s1=''
        for i in s:
            if i=='(':
                stack.append(i)
                flag+=1
            elif i==')':
                if flag >0:
                    stack.append(i)
                    flag-=1
            else:
                stack.append(i)

        s1="".join(stack)
        print s1
        s1=s1[::-1]
        print s1,flag
        s1=s1.replace('(','',flag)
        return s1[::-1]

a=Solution()
ans=a.minRemoveToMakeValid('))((')
print ans
