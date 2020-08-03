from collections import Counter
try:
    for _ in range(int(input())):
        n=int(input())
        xx,yy=[],[]
        ansx,ansy=0,0
        for i in range(4*n-1):
            x,y=map(int,input().split())
            xx.append(x)
            yy.append(y)
        cx=Counter(xx)
        cy=Counter(yy)
        c=cx.most_common()
        d=cy.most_common()
        for i,j in c:
            if j%2==1:
                ansx=i
                break
        for i,j in d:
            if j%2==1:
                ansy=i
                break
        print(ansx,ansy)
            
        
                
            
            
            
        
            
except:
    pass
