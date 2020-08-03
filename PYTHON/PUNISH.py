try:
    for _ in range(int(input())):
        n,k=map(int,input().split())
        q=k//n
        if q%2==0:
            print(k%n)
        else:
            pass
except:
    pass
