try:
    for _ in range(int(input())):
        n,k=map(int,input().split())
        arr=[int(i) for i in input().split()]
        T_rev=sum(arr)
        for i in range(n):
            if arr[i]>k:
                arr[i]=k
        R_rev=sum(arr)
        loss=T_rev-R_rev
        print(loss)
except:
    pass
