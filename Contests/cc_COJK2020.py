import math
from collections import Counter
try:
    for _ in range(1):
        n,k=map(int,input().split())
        arr=[int(i) for i in input().split()]
        m=max(arr)
        tem=[]
        k=k-1
        for i in range(1,m):
            sm=0
            for j in range(n):
                sm+=abs(i-arr[j])
            tem.append(sm)
        print(min(tem)-k)
                
        
except:
    pass
