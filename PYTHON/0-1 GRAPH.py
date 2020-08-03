def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def BFS(adj,src,n,d):
    visited=[False]*(n+1)
    dist=0
    d[src]=dist
    visited[src]=True
    Q=[]
    Q.append(src)
    while len(Q)>0:
        x=Q.pop(0)
        for i in adj[x]:
            if not visited[i]:
                visited[i]=True
                Q.append(i)
                d[i]=d[x]+1
    mn=float('inf')
    sm=0
    for i in range(n,0,-1):
        if d[i]>mn:d[i]=mn
        mn=min(mn,d[i])
        sm+=d[i]
    return sm

        
try:
    n,m=map(int,input().split())
    adj=[[] for i in range(n+1)]
    for i in range(m):
        u,v=map(int,input().split())
        addEdge(adj,u,v)
    d=[0]*(n+1)
    ans=BFS(adj,1,n,d)
    print(ans)
except:
    pass
