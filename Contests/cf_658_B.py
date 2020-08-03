import math
from collections import Counter
try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        c=arr.count(1)
        if n%2==0 and c==n:
            print("Second")
        elif n%2!=0 and c==n:
            print("First")
        else:
            ans=0
            for i in range(n):
                if arr[i]>1:
                    break
                else:
                    ans=1-ans
            if ans:
                print("Second")
            else:
                print("First")
            
                    


                
                
                
                
        
except:
    pass
