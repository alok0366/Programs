import sys
import math
from collections import Counter
import heapq
for _ in range(1):
    n=int(input())
    s=list(input())
    ptr=0
    while(ptr<n and s[ptr]=="R"):ptr+=1
    if ptr==n:
        print(0)
        exit(0)
    k=ptr
    ptr=n-1
    while(ptr>=0 and s[ptr]=="W"):
        ptr-=1
    if ptr==-1:
        print(0)
        exit(0)
    l=ptr
    ans=0
    while(k<l):
        if s[k]=="W" and s[l]=="R":
            s[k],s[l]=s[l],s[k]
            k+=1
            l-=1
            ans+=1

        elif s[k]=="R":
            k+=1
        elif s[l]=="W":
            l-=1
    print(ans)
    
        
