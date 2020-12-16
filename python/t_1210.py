def lemonadeChange(bills):
    change={5:0,10:0}
    for i in bills:
        if i==5:
            change[5]+=1
        elif i==10:
            if change[5]<=0:
                return False
            else:
                change[5]-=1
                change[10]+=1
       
        elif i==20:
            if change[10]<=0 and change[5]>=3:
                change[5]-=3
            if change[10]>0 and change[5]>0:
                change[10]-=1
                change[5]-=1
            else:
                return False
    return True
bills=[5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print lemonadeChange(bills)
