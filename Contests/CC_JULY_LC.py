import math
from collections import Counter
try:
    for _ in range(int(input())):
        n,m,x,y=map(int,input().split())
        if n==m==1:
            print(x)
            continue
        if y==x:
            z=n*m
            if z%2==0:
                print((z//2)*x)
            else:
                print(((z//2)+1)*x)
        elif y<x:
            z=n*m
            if z%2==0:
                z=z//2
                print((z*y))
            else:
                z=z//2
                print((z+1)*y)
        else:
            if x*2<=y:
                print(n*m*x)
            else:
                diff=y-x
                z=n*m
                if z%2==0:
                    z=z//2
                    print((z*x+z*diff))
                else:
                    z=z//2
                    print((z+1)*x+z*diff)
            
            
except:
    pass
