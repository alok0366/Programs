try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        arr.sort()
        flg=0
        ans=-1
        for i in range(1,1024):
            tem=[]
            for j in range(n):
                tem.append(arr[j]^i)
            tem.sort()
            for k in range(n):
                if arr[k]!=tem[k]:
                    break
            else:
                ans=i
                break
        print(ans)
                
                    
            
                
                
            
                
                
        
        
        
        
        
        
        

except:
    pass
