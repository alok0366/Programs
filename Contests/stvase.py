import math
def minSwaps(arr): 
    n = len(arr) 
    arrpos = [*enumerate(arr)] 
    arrpos.sort(key = lambda it:it[1]) 
    vis = {k:False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]: 
            vis[j] = True
            j = arrpos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans 

def swapPositions(p, pos1, pos2):
    p[pos1], p[pos2] = p[pos2],p[pos1] 
    return p

def robotwork(p,md,m,p2):
    flg=0
    while(p[:]!=p2[:] and flg<=m):
        for ra in md:
            if p[ra[1]-1]<p[ra[0]-1]:
                swapPositions(p,ra[1]-1,ra[0]-1)
                flg=0
            else:
                flg+=1
                
    
  

try:
    for _ in range(int(input())):
        n,m=[int(i) for i in input().split()]
        p=[int(i) for i in input().split()]
        md=[]
        for i in range(m):
            x=[int(i) for i in input().split()]
            md.append(sorted(x))
        if m==0:
            print(minSwaps(p)) 
        else:
            if n<=5:
                p2=sorted(p)
                mn=[]
                robotwork(p,md,m,p2)
                mn.append(minSwaps(p))
                for i in range(n-1):
                    for j in range(i+1,n-1):
                        if p[j]>p[i]:
                            swapPositions(p,j, i)
                            robotwork(p,md,m,p2)
                            mn.append(minSwaps(p))
                print(min(mn))
                            
                


                
            else:
                pass
except:
    pass
