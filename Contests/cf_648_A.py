import math
def isKthBitSet(n, k): 
    if n & (1 << (k - 1)): 
        return 1 
    else: 
        return 0 

try:
    n=int(input())
    arr=[int(i) for i in input().split()]
    arr.sort()
    tem1=arr[n-1]
    tem2=0
    for i in range(n-2,-1,-1): 
        if isKthBitSet(arr[i],2):
            tem2=arr[i]
            break
    print(tem1|tem2)





        
except:
    pass
