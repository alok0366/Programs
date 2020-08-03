def addEdge(adj,u,v):
    adj[u].append(v)
def DFS(adj,src,n):
    visited=[False]*n
    S=[]
    S.append(src)
    visited[src]=True
    while len(S)>0:
        u=S.pop()
        print(u,end=" ")
        for i in adj[u]:
            if not visited[i]:
                S.append(i)
                visited[i]=True
            
        
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
    
    
