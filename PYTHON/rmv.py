if __name__=="__main__":
    for _ in range(int(input())):
        n,k=map(int,input().split())
        start=(1+2*k)%n
        lst=[]
        for i in range(1,n+1):
            lst.append(i)
        itr=start
        while(len(lst)!=1):
            print(lst)
            lst.remove(itr)
            start=(start+2-1)%len(lst)
            itr=itr+start
        print(lst[0])
            
                
            
                    
                
                
                
            
