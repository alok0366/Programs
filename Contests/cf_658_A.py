import math
from collections import Counter
try:
    for _ in range(int(input())):
        m,n=map(int,input().split())
        a=[int(i) for i in input().split()]
        b=[int(i) for i in input().split()]
        flg=0
        for i in range(m):
            for j in range(n):
                if a[i]==b[j]:
                    print("YES")
                    print(1,b[j])
                    flg=1
                    break
            if flg:
                break
        if flg==0:
            print("NO")
 
 
        
except:
    pass
