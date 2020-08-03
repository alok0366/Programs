try:
    m,n=map(int,input().split())
    dp=[[1 for j in range(n)] for i in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[-1][-1])
except:
    pass
