try:
    for _ in range(int(input())):
        n,m,k=map(int,input().split())
        temp={}
        for i in range(n):
            a=[0]*(m+1)
            x=list(map(int,input().split()))
            for j in x:
                a[j]=a[j]+1
            z=max(a)
            c=a.count(z)
            if c==1:
                temp[i]=a.index(z)
            else:
                mxc=0
                for k in range(len(a)):
                    if a[k]==z:
                        mxc+=1
                    if mxc==2:
                        temp[i]=k
                        break
        for i in temp:
            print(temp[i],end=" ")                
except:
    pass
