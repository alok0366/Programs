def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def BFS(adj,src,n,values):
    visited=[False]*(n+1)
    Q=[]
    values[src]=0
    Q.append(src)
    visited[src]=True
    while len(Q)>0:
        x=Q.pop(0)
        for i in adj[x]:
            if not visited[i]:
                Q.append(i)
                visited[i]=True
                values[i]=values[x]+1
                
    
        
try:
    for _ in range(int(input())):
        n=int(input())
        adj=[[] for i in range(n+1)]
        values=[0]*(n+1)
        for i in range(n-1):
            u,v=map(int,input().split())
            addEdge(adj,u,v)
        BFS(adj,1,n,values)
        ans=[0]*(n+1)
        for i in range(1,n+1):
            if values[i]%2==0:
                ans[i]=1971894656414957547
            else:
                ans[i]=1169214570588269810
        ans.pop(0)
        print(*ans)
except:
    pass
    
    
