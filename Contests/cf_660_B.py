import sys
import math
from collections import Counter
import heapq
try:
    for _ in range(int(input())):
        n=int(input())
        a=""
        x=(n// 4)+((n % 4)!=0)
        a="9"*(n-x)+"8"*x
        print(a)
except:
    pass
