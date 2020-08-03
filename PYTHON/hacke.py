try:
    for _ in range(int(input())):
        n,k=[int(i) for i in input().split()]
        tem=int(n/k)
        ans=n*(n+1)//2
        while(tem>=1):
            ans-=(k*(tem*(tem+1)))//2
            ans+=(tem*(tem+1))//2
            tem=tem//k
        print(ans)
        
except:
    pass
