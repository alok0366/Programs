cost=[]
flg=0
def add_edge(adj,x, y): 
    adj[x].append(y) 
    adj[y].append(x) 
def BFS(adj, src,dest,v,pred,dist):
    queue=[]
    visited=[0]*(v+1)
    #print('inside BFS')
    for i in range(v):
        visited[i]=False
        dist[i]=float('inf')
        pred[i]=-1
    #print('above error')
    visited[src]=True
    dist[src]=0
    queue.append(src)
    #print('below BFS')
    while(len(queue)):
        u=queue.pop(0)
        for j in range(len(adj[u])):
            if visited[adj[u][j]]==False:
                visited[adj[u][j]]=True
                dist[adj[u][j]]=dist[u]+1
                pred[adj[u][j]]=u
                queue.append(adj[u][j])
                if adj[u][j]==dest:
                    return True
    return False

def printsd(adj,s,dest,v,path):
    pred,dist=[0]*(v+1),[0]*(v+1)
    #print('inside printsd')
    if(BFS(adj,s,dest,v,pred,dist)==False):
        return
    crawl=dest
    #print('below printsd')
    path.append(crawl)
    while(pred[crawl]!=-1):
        path.append(pred[crawl])
        crawl=pred[crawl]
    sm=0
    for i in range(len(path)-1,0,-1):
        sm+=cost[path[i]]
    print(sm)
        


try:
    n,q=map(int,input().split())
    adj=[[] for i in range(n+1)]
    cost=[]
    for i in range(n-1):
        x,y,c=map(int,input().split())
        add_edge(adj,x, y)
        cost.append(c)
    for j in range(q):
        qq=list(map(int,input().split()))
        path=[]
        if len(qq)==3:
            printsd(adj,qq[1],qq[2],n,path)
        else:
            c=qq[1]
            temp=adj[c]
            l=len(temp)
            for i in range(l-1):
                cost[temp[i]]*=c
            cost[temp[l-1]-1]*=c
except:
    pass
      
