def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def DFS_rec_cycle(adj,src,visited,parent):
    visited[src]=True
    for i in adj[src]:
        if visited[i] and i!=parent:
            return True
        if not visited[i] and DFS_rec_cycle(adj,i,visited,src):
            return True
    return False


    
def DFS(adj,src,n):
    visited=[False]*n
    for i in range(n):
        if not visited[i] and DFS_rec_cycle(adj,i,visited,-1):
            return True
    return False



try:
    print("PROGRAM TO DETECT CYCLE IN AN UNDIRECTED GRAPH")
    print("HOW MANY EDGES U HAVE")
    n=int(input())
    adj=[[] for i in range(n+1)]
    print("ENTER DETAILS OF EDGE U TO V")
    for i in range(1,n+1):
        u,v=map(int,input().split())
        addEdge(adj,u,v)
    print(DFS(adj,1,n+1))
except:
    pass
    
    
