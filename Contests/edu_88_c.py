try:
    for _ in range(int(input())):
        h,c,t=map(int,input().split())
        if h<=t:
            print(1)
        elif h+c>=2*t:
            print(2)
        else:
            x=int((c-t)/(h+c-2*t))
            m=abs((x*(h+c-2*t)+t-c)/(2*x-1))
            n=abs(((x+1)*(h+c-2*t)+t-c)/(2*(x+1)-1))
            if m<=n:
                print(2*x-1)
            else:
                print(2*x+1)
    
except:
    pass
