def oushu(begin,end):
    sum=0
    list=[]
    for i in range(begin,end+1):
        if i%2==0:
            sum+=i
            list.append(i)
    return list,sum
print(oushu(20,46))

