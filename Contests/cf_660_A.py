import sys
import math
from collections import Counter
import heapq
try:
    for _ in range(int(input())):
        a=6;b=10;c=14;d=15;e=21
        n=int(input())
        if (n < (a + b + c) + 1):print("NO")
        else:
            if (n - a - b - c != a and n - a - b - c != b and n - a - b - c != c):
                print("YES")
                print(a,b,c,(n - a - b - c))
            else:
                c=d
                if (n - a - b - c != a and n - a - b - c != b and n - a - b - c != c):
                    print("YES")
                    print(a,b,c,(n - a - b - c))
                else:
                    c=e
                    if (n - a - b - c != a and n - a - b - c != b and n - a - b - c != c):
                        print("YES")
                        print(a,b,c,(n - a - b - c))
            
except:
    pass
