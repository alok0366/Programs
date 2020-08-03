import math
from collections import Counter
try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        arr.sort(reverse=True)
        m1=arr[0]
        m2=arr[1]
        if m1>m2:
            print("WIN")
        elif m1==m2:
            print("DRAW")
        else:
            print("LOSE")
        
        
            
        





        
except:
    pass
