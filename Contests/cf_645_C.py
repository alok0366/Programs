try:
    for _ in range(int(input())):
        x1,y1,x2,y2=map(int,input().split())
        x_di=abs(x2-x1)
        y_di=abs(y2-y1)
        print(x_di*y_di+1)




except:
    pass
