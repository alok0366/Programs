def addEdge(adj,u,v):
    adj[u].append(v)
def DFS_REC(adj,s,visited,pos,time):
    visited[s]=True
    print(s,end=" ")
    time+=1
    for u in adj[s]:
        if not visited[u]:
            time=DFS_REC(adj,u,visited,pos,time)
    pos[s]=time
    time+=1
    return time
def DFS(adj,src,n):
    visited=[False]*n
    time=0
    pos=[0]*(n)
    for i in range(n):
        if not visited[i]:
            time=DFS_REC(adj,i,visited,pos,time)
    print(pos)
        
try:
    print("DFS TRAVSERSAL OF GRAPH")
    print("HOW MANY EDGES U HAVE")
    n=int(input())
    adj=[[] for i in range(n)]
    print("ENTER DETAILS OF EDGE U TO V")
    for i in range(n):
        u,v=map(int,input().split())
        addEdge(adj,u,v)
    #print("DFS TRAVERSAL IS:-",end=" ")
    
    DFS(adj,5,n)
except:
    pass
    
    
