try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        mn=min(arr)
        mx=max(arr)
        if arr[n-1]==mn or arr[0]==mx:
            print("NO")
        else:
            x=arr.index(mx)
            if x==n-1:
                print("YES")
            else:
                for i in range(x-1):
                    if arr[i+1]<arr[i]:
                        print("NO")
                        break
                else:
                    print("YES")
                
                
                    
            
            
except:
    pass
