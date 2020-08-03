st=[0]*(8*(10**5)
def buildtree(si,ss,se):
    if ss==se:
        st[si]=arr[ss]
    mid=(ss+se)//2
    buildtree(2*si,ss,mid)
    buildtree(2*si+1,mid+1,se)
    st[si]=max(st[2*si],st[2*si+1])

def query(si,ss,se,qs,qe):
    if (qs>se or qe<ss):
        return float('inf')
    if (ss>=qs and se<=qe):
        st[si]
    mid=(ss+se)//2
    l=query(2*si,ss,mid,qs,qe)
    r=query(2*si+1,mid+1,se,qs,qe)
    return max(l,r)

def update(si,ss,se,qi,val):
    if ss=se:
        st[si]=val
        return
    mid=(ss+se)//2
    if (qi<=mid):
        update(2*si,ss,mid,qi,val)
    else:
        update(2*si+1,mid+1,se,qi,val)
    st[si]=max(st[2*si],st[2*si+1])
    





try:
    N,Q=map(int,input().split())
    H=[int(i) for i in input().split()]
    A=[int(i) for i in input().split()]
    buildtree(1,1,N)
    for i in range(Q):
        t,b,x=map(int,input().split())
        if t==1:
            update(1,1,N,b,x)
        else:
            call find _max()
except:
    pass
