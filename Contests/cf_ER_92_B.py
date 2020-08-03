import sys
import math
from collections import Counter
import heapq
try:
    for _ in range(int(input())):
        s=input()
        co=[0]*10
        n,ans,m=len(s),0,0
        b=0
        for i in s:
            co[int(i)]+=1
        for i in range(10):
            for j in range(10):
                ans,b=0,0
                for k in range(n):
                    if b==0 and i==(int(s[k])):
                        b=1
                    elif j==(int(s[k])) and b==1:
                        b=0
                        ans+=2
                m=max(m,ans)
        for i in range(10):
            m=max(m,co[i])
        print(n-m)
        
        
        
except:
    pass
