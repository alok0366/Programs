try:
    for _ in range(int(input())):
        n,l=map(int,input().split())
        arr=[int(i) for i in input().split()]
        ttr=0
        for i in range(n):
            ttr=ttr|arr[i]
        ttr=bin(ttr).count("1")
        if ttr<l:
            print(-1)
        else:
            pass
            

except:
    pass
