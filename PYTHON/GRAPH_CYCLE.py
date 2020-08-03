def addEdge(adj,u,v):
    adj[u].append(v)

def DFS_rec_cycle(adj,src,visited):
    visited[src]=1
    for i in adj[src]:
        if visited[i]==1:
            return True
        if visited[i]==0 and DFS_rec_cycle(adj,i,visited):
            return True
    visited[src]=2
    return False


    
def DFS(adj,src,n):
    visited=[0]*n
    for i in range(n):
        if visited[i]==0 and DFS_rec_cycle(adj,i,visited):
            return True
    return False



try:
    print("PROGRAM TO DETECT CYCLE IN A GRAPH")
    print("HOW MANY EDGES U HAVE")
    n=int(input())
    adj=[[] for i in range(n)]
    print("ENTER DETAILS OF EDGE U TO V")
    for i in range(n):
        u,v=map(int,input().split())
        addEdge(adj,u,v)
    print(DFS(adj,0,n))
except:
    pass
    
    
