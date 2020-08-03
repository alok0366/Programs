try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        arr2=[int(i) for i in input().split()]
        ans=0
        dist=0
        dist2=0
        for i in range(n):
            dist+=arr[i]
            dist2+=arr2[i]
            if arr[i]==arr2[i] and dist==dist2:
                ans+=arr[i]
        print(ans)
        
except:
    pass
