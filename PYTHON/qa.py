try:
    for _ in range(int(input())):
        a,b=[int(i) for i in input().split()]
        if a<=b:
            print(1)
        else:
            if a%2==0:
                if a%b==0:
                    print(a//b)
                else:
                    print(a//b+1)
            else:
                if a%b==0:
                    print(a//b)
                else:
                    print(a)
except:
    pass
