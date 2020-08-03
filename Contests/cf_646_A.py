try:
    for _ in range(int(input())):
        n,x=map(int,input().split())
        arr=[int(i) for i in input().split()]
        even,odd=0,0
        for i in range(n):
            if arr[i]%2==0:
                even+=1
            else:
                odd+=1
        if odd==0:
            print("NO")
        elif odd%2==0:
            odd-=1
            while(odd and x>=1):
                odd-=1
                x-=1
            if x<=even:
                print("YES")
            else:
                print("NO")
        else:
            while(odd and x>=1):
                odd-=1
                x-=1
            if x<=even:
                print("YES")
            else:
                print("NO")
except:
    pass
