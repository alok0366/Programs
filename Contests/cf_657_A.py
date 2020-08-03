try:
    for _ in range(int(input())):
        l,r,m=map(int,input().split())
        a=l
        mod=m%l
        c=l
        b=c+mod
        if m-(b-c)==0:
            print(a,c,b)
        else:
            print(a,b,c)
except:
    pass
