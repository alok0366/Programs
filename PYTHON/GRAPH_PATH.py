def addEdge(adj,u,v):
    adj[u].append(v)
def DFS_REC(adj,s,visited,tem):
    visited[s]=True
    tem.append(s)
    for u in adj[s]:
        if not visited[u]:
            DFS_REC(adj,u,visited,tem)
    return tem
def DFS(adj,src,n):
    visited=[False]*n
    path=[]
    for i in range(n):
        if not visited[i]:
            tem=[]
            x=DFS_REC(adj,i,visited,tem)
            path.append(x)
    return path
        
try:
    print("ALL POSSIBLE PATH FROM ANY NODE")
    print("HOW MANY EDGES U HAVE")
    n=int(input())
    adj=[[] for i in range(n)]
    print("ENTER DETAILS OF EDGE U TO V")
    for i in range(n):
        u,v=map(int,input().split())
        addEdge(adj,u,v)
    path=DFS(adj,0,n)
    print(path)
except:
    pass
    
    
