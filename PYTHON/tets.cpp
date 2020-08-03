for i in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    k=n-1
    while k>0 and m[k-1]>=m[k]:k-=1
    while k>0 and m[k-1]<=m[k]:k-=1
    print(k)
