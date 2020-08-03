try:
    for _ in range(int(input())):
        a,b,n,m=map(int,input().split())
        p,q,r,s=a,b,n,m
        if a>b:
            a=a-n
        else:
            b=b-n
        if a>b:
            b=b-m
        else:
            a=a-m
        if a>=0 and b>=0:
            print("Yes")
        else:
            if p>q:
                q=q-s
            else:
                p=p-s
            if p>q:
                p=p-r
            else:
                q=q-r
            if p>=0 and q>=0:
                print("Yes")
            else:
                print("No")







        
except:
    pass
