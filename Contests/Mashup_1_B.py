import math
from collections import Counter
try:
    for _ in range(1):
        n=int(input())
        arr=[int(i) for i in input().split()]
        if n==1:
            print(-1)
        else:
            arr.sort()
            diff=arr[1]-arr[0]
            tem=[]
            for i in range(1,n):
                if (arr[i-1]+diff)==arr[i]:
                    continue
                else:
                    tem.append(arr[i-1]+diff)
            print(len(tem))
            print(*tem)
            
except:
    pass
