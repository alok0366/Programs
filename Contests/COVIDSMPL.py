import sys
try:
    for _ in range(int(input())):
        n,p=map(int,input().split())
        ans=[]
        print(1,1,1,n,n)
        tot=int(input())
        for i in range(1,n+1):
            tem=[0]*n
            if tot!=0:
                print(1,i,1,i,n)
                c=int(input())
                if c!=0:
                    for j in range(2,n+1):
                        print(1,i,j,i,n)
                        inf=int(input())
                        if c!=inf:
                            tem[j-2]=1
                            c-=1
                            tot-=1
                            if c==0:
                                break
                    if c!=0:
                        tem[n-1]=1
                        c-=1
                        tot-=1
                    if tot==0 or c==0:
                        ans.append(tem)
                        continue
                else:
                    ans.append(tem)
            else:
                ans.append(tem)
        print(2)
        for i in range(n):
            print(*ans[i])
        x=int(input())
        if x==-1:
            sys.exit(0)
        else:
            pass
except:
    pass
