try:
    for _ in range(1):
        n,k=map(int,input().split())
        t_book=[]
        al,bl=0,0
        for i in range(n):
            t,a,b=map(int,input().split())
            if a==1:
                al+=1
            if b==1:
                bl+=1
            t_book.append((t,a,b))
        if al<k or bl<k:
            print(-1)
        else:
            t_book.sort(key=lambda x:x[0])
            t2=[]
            x,y=0,0
            for i in range(n-1,-1,-1):
                if t_book[i][1]!=0 or t_book[i][2]!=0:
                    t2.append(t_book[i][0])
                if t_book[i][1]==1:
                    x+=1
                    if x>k:
                        t2.pop()
                elif t_book[i][2]==1:
                    y+=1
                    if y>k:
                        t2.pop()
                if x==k and y==k:
                    break
            print(sum(t2[:k-1]),t2)
                    
                
        
                
        
            







        
except:
    pass
