try:
    for _ in range(int(input())):
        a,b,n=[int(i) for i in input().split()]
        ans=0
        while(a<=n and b<=n):
            if a<b:
                a+=b
            else:
                b+=a
                
            ans+=1
        print(ans)
except:
    pass
