def longestWPI(hours):
    new_hour=[]
    for i in hours:
        if i >8:
            new_hour.append(1)
        else:
            new_hour.append(-1)
    pre_sum=[]
    pre_sum.append(0)
    for i in range(1,len(new_hour)+1):
        pre_sum.append(pre_sum[i-1]+new_hour[i-1])
    
    stack=[]
    for m in pre_sum:
hours=[9,9,6,0,6,6,9]
longestWPI(hours)
