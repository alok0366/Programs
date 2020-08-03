import sys
import math
from collections import Counter
import heapq
from queue import PriorityQueue
def addEdge(adj,u,v,w):
    adj[u].append((v,w))

def dijkstra(adj,src,dest,prev,dist):
    dist[src]=0
    pq=[(src,0)]
    #print(dist)
    while len(pq)>0:
        vertex,weight=heapq.heappop(pq)
        for nbh,wt in adj[vertex]:
            distance=weight+wt
            if distance<dist[nbh]:
                dist[nbh]=distance
                #print(dist[nbh])
                prev[nbh]=vertex
                heapq.heappush(pq,(nbh,distance))
                #print("alok")
    
    

try:
    print("PROGRAM TO FIND SHORTEST DISTANCE AND PATH IN A GRAPH(DJKSTRA)")
    print("HOW MANY VERTEX U WANT TO ENTER")
    nodes=int(input())
    print("HOW MANY EDGES U WANT TO ENTER ?")
    n=int(input())
    print("ENTER THE DETAILS OF THE EDGES FROM U TO V WITH ITS CORRESPONDING WEIGHTS FROM U TO V")
    adj=[[] for i in range(n+1)]
    #print(adj)
    for i in range(n):
        u,v,w=map(int,input().split())
        addEdge(adj,u,v,w)
    #print(adj)
    prev=[0]*(nodes+1)
    dist=[float('inf')]*(nodes+1)
    #print(prev,dist)
    dijkstra(adj,0,n+1,prev,dist)
    print(dist)
    print(prev)
except:
    pass
    
