import sys
try:
    for _ in range(int(input())):
        n,p=map(int,input().split())
        ans=[]
        print(1,1,1,n,n)
        tot=int(input())
        c_1=0
        tt=tot
        for i in range(1,n):
            tem=[0]*n
            if tt!=0:
                print(1,i,1,i,n)
                r_tot=int(input())
                if r_tot!=0:
                    for j in range(1,n):
                        print(1,i,j+1,n,n)
                        s1=int(input())
                        print(1,i+1,1,n,j)
                        s2=int(input())
                        if s1+s2+c_1!=tot:
                            tem[j-1]=1
                            c_1+=1
                    print(1,i+1,1,n,n-1)
                    s1=int(input())
                    print(1,i+1,n,n,n)
                    s2=int(input())
                    #print(s1,s2,c_1)
                    if s1+s2+c_1!=tot:
                        tem[n-1]=1
                        c_1+=1
                        tt-=1
                    ans.append(tem)
                else:
                    ans.append(tem)
            else:
                ans.append(tem)
        print(1,n,1,n,n)
        c=int(input())
        tem=[0]*n
        if c!=0:
            for i in range(2,n+1):
                print(1,n,i,n,n)
                inf=int(input())
                if c!=inf:
                    tem[i-2]=1
                    c-=1
                    if c==0:
                        ans.append(tem)
                        break
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
            
            
            
            







