import sys
import math
from collections import Counter
import heapq
try:
    for _ in range(int(input())):
        l,r=map(int,input().split())
        x=l
        y=l*2
        if y>r:
            print(-1,-1)
        else:
            print(x,y)
        
except:
    pass
