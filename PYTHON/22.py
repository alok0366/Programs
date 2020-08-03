try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        ans=0
        arr2=arr.copy()
        arr2.sort()
        for i in range(n):
            if arr[i]!=arr2[i]:
                ans+=1
        print(ans//2)
except:
    pass
