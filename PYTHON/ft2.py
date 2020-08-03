if __name__=="__main__":
    n,q=map(int,input().split())
    path={}
    cost={}
    for i in range(n-1):
        x,y,c=map(int,input().split())
        path.setdefault(i,[]).append(y)
        cost[i]=c
    for i in range(q):
        qq=list(map(int,input().split()))
        if len(qq)==3:
            src=qq[1]
            dest=qq[2]
            for j in path:
                for k in path[j]:
                    if k==
        
