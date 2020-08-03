try:
    poss,imposs=0,0
    for _ in range(int(input())):
        s,n,k,r=map(int,input().split())
        if r==1:
            c_r=n*k
            if c_r>s:
                print("IMPOSSIBLE",c_r-s)
                imposs+=c_r-s
            else:
                print("POSSIBLE",s-c_r)
                poss+=s-c_r
        else:
            c_r=(k*(1-r**n))//(1-r)
            if c_r>s:
                print("IMPOSSIBLE",c_r-s)
                imposs+=(c_r-s)
            else:
                print("POSSIBLE",s-c_r)
                poss+=(s-c_r)
    if poss<imposs:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
            
except:
    pass
        
