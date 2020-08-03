def addEdge(adj,u,v):
    adj[u].append(v)
def DFS_REC(adj,s,visited):
    visited[s]=True
    print(s,end=" ")
    for u in adj[s]:
        if not visited[u]:
            DFS_REC(adj,u,visited)
def DFS(adj,src,n):
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            DFS_REC(adj,i,visited)
        
try:
    print("DFS TRAVSERSAL OF GRAPH")
    print("HOW MANY EDGES U HAVE")
    n=int(input())
    adj=[[] for i in range(n)]
    print("ENTER DETAILS OF EDGE U TO V")
    for i in range(n):
        u,v=map(int,input().split())
        addEdge(adj,u,v)
    print("DFS TRAVERSAL IS:-",end=" ")
    
    DFS(adj,0,n)
except:
    pass
    
    
