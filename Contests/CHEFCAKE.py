try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        arr.sort(reverse=True)
        ans=1
        mx=arr[0]
        for i in range(1,n):
            if arr[i]<mx:
                mx=arr[i]
                continue
            else:
                ans+=1
        print(ans)
except:
    pass
        
