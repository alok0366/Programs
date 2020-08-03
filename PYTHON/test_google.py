try:
    T=int(input())
    for t in range(1,T+1):
        n=int(input())
        arr=[int(i) for i in input().split()]
        mx=-1
        days=0
        for i in range(n):
            if arr[i]>mx:
                mx=arr[i]
                if i==n-1 or arr[i]>arr[i+1]:
                    days+=1
                    
        print("Case #{}: {}".format(t, days))
except:
    pass
