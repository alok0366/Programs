try:
    for _ in range(int(input())):
        n=int(input())
        d1,d2,d3={},{},{}
        mx=float('inf')
        arr_a=[int(i) for i in input().split()]
        arr_b=[int(i) for i in input().split()]
        for i in range(n):
            d1[arr_a[i]]=0
            d1[arr_b[i]]=0
        for i in range(n):
            mx=min(arr_a[i],mx)
            d1[arr_a[i]]+=1
        for i in range(n):
            mx=min(arr_b[i],mx)
            d1[arr_b[i]]+=1
        flg=0
        for i in d1:
            if d1[i]%2==1:
                flg=1
                break
            else:
                d2[i]=d1[i]//2
        if flg:
            print(-1)
            continue
        else:
            d3=d2.copy()
            L1,L2=[],[]
            for i in range(n):
                if d2[arr_a[i]]:
                    d2[arr_a[i]]-=1
                else:
                    L1.append(arr_a[i])
            for i in range(n):
                if d3[arr_b[i]]:
                    d3[arr_b[i]]-=1
                else:
                    L2.append(arr_b[i])
            L1.sort()
            L2.sort(reverse=True)
            s=len(L1)
            if s==0:
                print(0)
            else:
                ans=0
                for i in range(s):
                    ans+=min(2*mx,min(L1[i],L2[i]))
                print(ans)
                
except:
    pass

            
                

