try:
    for _ in range(int(input())):
        n,m,k=map(int,input().split())
        c_pp=n//k
        if c_pp>=m:
            print(m)
        else:
            r_j=m-c_pp
            r_p=k-1
            if r_j%r_p==0:
                print(c_pp-(r_j//r_p))
            else:
                print(c_pp-((r_j//r_p)+1))
except:
    pass
