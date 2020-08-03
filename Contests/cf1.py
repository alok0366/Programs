try:
    n,s=[int(i) for i in input().split()]
    arr=[1 for i in range(n-1)]
    sm=sum(arr)
    arr.append(abs(s-sm))
    if s>=2*n:
        print("YES")
        print(*arr)
        print(s//2)
    else:
        print("NO")
except:
    pass
    
