import math
try:
    c=int(input())
    time=[]
    for i in range(c):
        x,y,v=map(int,input().split())
        dist=(x**2+y**2)
        dist=math.sqrt(dist)
        time.append(dist/v)
    y=set(time)
    ans=0
    for i in y:
        n=time.count(i)
        if n>=2:
            ans+=(n*(n-1))//2
    print(ans)
        
        
except:
    pass
