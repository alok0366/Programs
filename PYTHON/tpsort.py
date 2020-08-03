def swapPositions(p, pos1, pos2,pos3):
    p[pos1], p[pos2],p[pos3] = p[pos3],p[pos1],p[pos2]
    return p

try:
    for _ in range(int(input())):
        n,k=[int(i) for i in input().split()]
        p=[int(i) for i in input().split()]
        if (n//2)%2:
            print(-1)
        elif k<n//2:
            print(-1)
        else:
            print(n//2)
            turn=0
            ptr1=0
            ptr2=1
            for i in range(n//2):
                if turn==2:
                    ptr1+=2
                    ptr2+=2
                    turn=0
                if turn!=2:
                    print(p[n-i-1],p[ptr2],p[ptr1])
                    turn+=1
                
except:
    pass
