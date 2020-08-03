def addEdge(adj,u,v):
    adj[u].append(v)
def BFS(adj,src,n):
    Q=[]
    visited=[False]*n
    Q.append(src)
    visited[src]=True
    while len(Q)>0:
        v=Q.pop(0)
        print(v,end=" ")
        for u in adj[v]:
            if not visited[u]:
                Q.append(u)
                visited[u]=True
try:
    print("BFS TRAVSERSAL OF GRAPH")
    print("HOW MANY EDGES U HAVE")
    n=int(input())
    adj=[[] for i in range(n)]
    print("ENTER DETAILS OF EDGE U TO V")
    for i in range(n):
        u,v=map(int,input().split())
        addEdge(adj,u,v)
    print("BFS TRAVERSAL IS:-",end=" ")
    BFS(adj,0,n)
except:
    pass
    
    
