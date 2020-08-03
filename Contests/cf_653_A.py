try:
    for _ in range(int(input())):
        n=int(input())
        flg,c=0,0
        while(n!=1):
            if(n&(n-1))==0:
                print(-1)
                flg=1
                break
            elif n%6==0:
                n=n//6
            else:
                n=n*2
            c+=1
        if flg==0:
            print(c)
                
            







        
except:
    
    pass
