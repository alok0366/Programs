import math
from collections import Counter
try:
    for _ in range(1):
        n,k,m=map(int,input().split());
        arr=[int(i) for i in input().split()]
        arr2=[*enumerate(arr)]
        arr2.sort(reverse=True,key=lambda x:x[1])
        tem=[]
        for i in range(k):
            tem.append(arr2[i])
        tem.sort(key=lambda x:x[0])
        mod=[i%m for i in range(1,k+1)]
        ans=0
        for i in range(k):
            ans+=tem[i][1]*mod[i]
        print(ans)
            
        


        
except:
    pass
