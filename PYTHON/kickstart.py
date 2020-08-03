try:
    T = int(input())
    for t in range(1, T + 1):
        r,c=map(int,input().split())
        mat=[]
        for i in range(r):
            tem=input()
            mat.append(tem)
        print(mat)
        
        
        
        print("Case #{}: {}".format(t,ans))
except:
    pass
