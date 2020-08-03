try:
    for _ in range(int(input())):
        st=input()
        if len(st)==1 or len(st)==2:
            print("YES")
        else:
            if len(st)%2==0:
                print(st[len(st)/2:])
                if st[:len(st)/2]==st[len(st)/2:]:
                    print("YES")
                else:
                    print("NO")
            else:
                if st[:len(st)/2]==st[(len(st)/2)+1:]:
                    print("YES")
                else:
                    print("NO")
    

        
        





except:
    pass
