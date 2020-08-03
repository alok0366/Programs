def subarrayBitwiseOR(A): 
    # res contains distinct values 
    res = set() 
  
    pre = {0} 
  
    for x in A: 
        pre = {x | y for y in pre} | {x}
        print(pre)
        res |= pre 
  
    return len(res) 
  

import math
from collections import Counter
try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        ans=(subarrayBitwiseOR(arr))
        if ans==(n*(n+1))//2:
            print("YES")
        else:
            print("NO")
            





        
except:
    pass
