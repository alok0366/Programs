try:
    for _ in range(int(input())):
        n=int(input())
        ans=[]
        ptr=0
        for i in range(1,n+1):
            tem=[]
            if i%2==0:
                for j in range(n,0,-1):
                    ptr+=1
                    tem.insert(0,ptr)
            else:
                for j in range(1,n+1):
                    ptr+=1
                    tem.append(ptr)
            ans.append(tem)
        for i in range(n):
            print(*ans[i])
                
except:
    pass
