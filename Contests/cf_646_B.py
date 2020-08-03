try:
    for _ in range(int(input())):
        s=input()
        l=len(s)
        c_0=s.count("0")
        c_1=s.count("1")
        mn=0
        if c_0>=c_1:
            mn=c_1
        else:
            mn=c_0
        if mn==c_0:
            c=0
            for i in range(len(s)):
                if s[i]=="0":
                    c+=1
        else:
            c=0
            for i in range(1,len(s)):
                if s[i]=="1":
                    c+=1
        if int(s,2)!=1:
            print(c)
        else:
            print(0)
                    
            
            



            
except:
    pass
