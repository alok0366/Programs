#python program to implement minimum no of swaps to sort an arry when no is in (1-n)
def MinSwap(arr,n):
    arrpos=[*enumerate(arr)]
    vis=[False for i in range(n)]
    ans=0
    for i in range(n):
        if vis[i] or arrpos[i][1]==i+1:
            continue
        c_s=0
        vis[i]=True
        j=arrpos[i][1]-1
        while not vis[j]:
            vis[j]=True
            j=arrpos[i][1]-1
            c_s+=1
        if c_s>0:
            ans+=c_s
    return ans
        





try:
    print("ENTER THE LENGTH OF ARRAY FOR WHICH U WANT TO FIND MINIMUM SWAPS TO SORT IT:-")
    n=int(input())
    print("NOW ENTER THE VALUES SEPERATED BY SPACE:-")
    arr=[int(i) for i in input().split()]
    print("MINIMUM NO OF SWAPS REQUIRED TO SORT THE ARRAY IS: {}".format(MinSwap(arr,n)))
except:
    pass
