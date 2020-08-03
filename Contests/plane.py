if __name__=="__main__":
    n,m=map(int,input().split())
    g=list(map(int,input().split()))
    p=list(map(int,input().split()))
    g.sort()
    p.sort()
    if p[m-1]<g[n-1]:
        print(-1)
    else:
        ptr1,ans=0,0
        while(ptr1!=n):
            ptr2=0
            for i in range(len(p)):
                if g[ptr1]<=p[ptr2]:
                    ptr1+=1
                    ptr2+=1
                else:
                    p.pop(0)
            ans+=2
        print(ans-1)
                    
                    
                    
