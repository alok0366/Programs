try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        ans=n-1
        while ans>0 and arr[ans-1]>=arr[ans]:
            ans-=1
        while ans>0 and arr[ans-1]<=arr[ans]:
            ans-=1
        print(ans)
        
except:
    pass
