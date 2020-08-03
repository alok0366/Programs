try:
    n,k=map(int,input().split())
    arr=[int(i) for i in input().split()]
    if k>=n:
        print(max(arr))
    else:
        for i in arr:
            if i>k:
                print(i)
                break
            
        
except:
    pass
