import math
from collections import Counter
def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def bfs(adj,src):
    




try:
    for _ in range(int(input())):
        n=int(input())
        adj=[[] for i in range(n)]
        for i in range(n-1):
            a,b=map(int,input().split())
            addEdge(adj,a,b)
        col=[int(i) for i in input().split()]
        de=[int(i) for i in input().split()]
        ans=[]
        visited=[0]*n
        for i in range(n-1):
            ans2=bfs(adj,de[i],col,visited)
            ans.append(ans2)
        for i in ans:
            print(i)
except:
    pass
            
            
        



        
except:
    pass
