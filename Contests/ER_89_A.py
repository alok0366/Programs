try:
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if a!=0 and b!=0:
            if a<b:
                a,b=b,a
            if b>=a//2:
                print(max(a//2+(b-(a//2)),(b//2)+(a-(b//2))))
            else:
                print(b)
        else:
            print(0)
except:
    pass

