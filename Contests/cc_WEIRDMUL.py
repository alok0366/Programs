def W(l,r,arr,x):
    tem=0
    for i in range(l,r+1):
        tem+=arr[i-1]*((x)**(i-l))
    print(tem,end=" ")
    return tem


def mmm(a,b,m):
    res=0
    a%=m
    while(b):
        if(b&1):
            res=(res+a)%m
        a=(2*a)%m
        b>>=1
    return res

def pw(a,b,c):
    ans=1
    a=a%c
    if a==0:
        return 0
    while(b>0):
        if(b&1):
            ans=(ans*a)%c
        b=b>>1
        a=(a*a)%c
    return ans

try:
    for _ in range(int(input())):
        M=998244353
        n,x=map(int,input().split())
        arr=[int(i) for i in input().split()]
        ans=1
        for i in range(1,n+1):
            for j in range(i,n+1):
                ans*=((W(i,j,arr,x))**2)
                #print(ans)
        print()
        print(ans%M)
except:
    pass
                
