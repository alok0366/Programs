try:
    n=int(input())
    print(1,end=" ")
    tem=[]
    tem.append(1)
    c=1
    for i in range(1,n):
        print(c+i,end=" ")
        tem.append(c+i)
        c=c+(n+1%i)
    sum=[]
    for i in range(n):
        sm=0
        for j in range(i,n):
            sm+=tem[j]
            sum.append(sm)
    sum.sort()
    print(sum)
except:
    pass
