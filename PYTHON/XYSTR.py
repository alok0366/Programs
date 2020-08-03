try:
    for _ in range(int(input())):
        s=input()
        c=0
        l=len(s)
        ptr=0
        while(ptr<l-1):
            if s[ptr]=="x" and s[ptr+1]=="y":
                c+=1
                ptr+=2
                continue
            elif s[ptr]=="y" and s[ptr+1]=="x":
                c+=1
                ptr+=2
                continue
            ptr+=1
        print(c)
except:
    pass
