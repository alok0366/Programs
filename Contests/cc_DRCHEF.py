try:
    for _ in range(int(input())):
        n,x=map(int,input().split())
        pop=[int(i) for i in input().split()]
        pop.sort()
        lf,rf=[],[]
        for i in range(n-1,-1,-1):
            if pop[i]>=x:
                lf.append(pop[i])
            else:
                if pop[i]*2>=x:
                    lf.append(pop[i])
                else:
                    rf.append(pop[i])
        lf.sort()
        rf.sort(reverse=True)
        for i in range(len(rf)):
            lf.append(rf[i])
        ans=0
        for i in range(n):
            while(lf[i]>x):
                x=2*x
                ans+=1
            x=lf[i]*2
            ans+=1
        print(ans)
            
except:
    pass
