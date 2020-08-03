#start as beginner end as pro<**viper95**>
try:
    for _ in range(int(input())):
        temp=0
        us=float('-inf')
        a=[int(i) for i in input().split()]
        b=[int(i) for i in input().split()]
        add=[0]*3
        mul=[0]*3
        rem=[0]*3
        for i in range(3):
            add[i]=b[i]-a[i]
            if(a[i]==0):
                mul[i]=us
            else:
                mul[i]=b[i]//a[i]
                rem[i]=b[i]%a[i]

        if(a[1]==b[1] and a[0]==b[0] and a[2]==b[2]):
            print(0)
            temp=1
        elif((add[0]==0 and add[1]==0) or (add[1]==0 and add[2]==0) or (add[2]==0 and add[0]==0)):
            print(1)
            temp=1
        elif(((add[0]==add[1]) and add[2]==0) or ((add[2]==add[1]) and add[0]==0) or ((add[0]==add[2]) and add[1]==0)):
            print(1)
            temp=1
        elif((rem[0]==0 and rem[1]==0 and (mul[0]==mul[1]) and add[2]==0 and mul[0]!=us) or (rem[1]==0 and rem[2]==0 and (mul[1]==mul[2]) and add[0]==0 and mul[2]!=us) or (rem[0]== 0 and rem[2]==0 and (mul[0]==mul[2]) and add[1]==0 and mul[0]!=us)):
            print(1)
            temp=1
        elif(add[0]==add[1]  and  add[1]==add[2]):
            print(1)
            temp=1
        elif(rem[0]==0  and  rem[1]==0  and  rem[2]==0  and  (mul[0]==mul[1])  and  (mul[1]==mul[2])  and  mul[0]!=us):
            print(1)
            temp=1
        elif(add[0]==0 or add[1]==0 or add[2]==0):
            print(2)
            temp=1
        elif(add[0]==add[1] or add[1]==add[2] or add[2]==add[0]):
            print(2)
            temp=1
        elif((rem[0]==0  and  rem[1]==0  and  mul[0]!=us  and  (mul[0]==mul[1])) or (rem[2]==0  and  mul[1]!=us  and  rem[1]==0  and  (mul[2]==mul[1])) or (rem[0]==0  and  mul[0]!=us  and  rem[2]==0  and  (mul[0]==mul[2]))):
            print(2)
            temp=1
        elif(((add[0]+add[1])==add[2]) or ((add[2]+add[1])==add[0]) or ((add[0]+add[2])==add[1])):
            print(2)
            temp=1
        elif(((rem[0]==0 and rem[1]==0 and rem[2]==0) and (mul[0]!=us and mul[1]!=us and mul[2]!=us) and (((mul[0]*mul[1])==mul[2]) or ((mul[2]*mul[1])==mul[0]) or ((mul[0]*mul[2])==mul[1])))):
            print(2)
            temp=1
        elif(((rem[2]==0) and (mul[2]!=us) and (b[0]==(add[1]+(a[0]*mul[2])))) or ((rem[1]==0) and (mul[1]!=us) and (b[0]==(add[2]+(a[0]*mul[1]))))):
            print(2)
            temp=1
        elif(((rem[2]==0) and (mul[2]!=us) and (b[1]==(add[0]+(a[1]*mul[2])))) or ((rem[0]==0) and (mul[0]!=us) and (b[1]==(add[2]+(a[1]*mul[0]))))):
            print(2)
            temp=1
        elif(((rem[0]==0) and (mul[0]!=us) and (b[2]==(add[1]+(a[2]*mul[0])))) or ((rem[1]==0) and (mul[1]!=us) and (b[2]==(add[0]+(a[2]*mul[1]))))):
            print(2)
            temp=1
        elif(((rem[1]==0) and (mul[1]!=us) and (b[0]==(mul[1]*(a[0]+add[2])))) or ((rem[2]==0) and (mul[2]!=us) and (b[0]==(mul[2]*(a[0]+add[1]))))):
            print(2)
            temp=1
        elif(((rem[0]==0) and (mul[0]!=us) and (b[1]==(mul[0]*(a[1]+add[2])))) or ((rem[2]==0) and (mul[2]!=us) and (b[1]==(mul[2]*(a[1]+add[0]))))):
            print(2)
            temp=1
        elif(((rem[1]==0) and (mul[1]!=us) and (b[2]==(mul[1]*(a[2]+add[0])))) or ((rem[0]==0) and (mul[0]!=us) and (b[2]==(mul[0]*(a[2]+add[1]))))):
            print(2)
            temp=1
        elif((b[1]==b[0])  and  (b[2]==b[0])):
            print(2)
            temp=1
        if(temp==0 and a[0]!=a[1]):
            x=(((b[0]-b[1])*(1.0))/(a[0]-a[1]));
            y=(((b[1]*a[0])-(a[1]*b[0])*(1.0))/(a[0]-a[1]));
            if(x==int(x)  and  y==int(y)  and  (b[2]==((a[2]*x)+y) or b[2]==(a[2]*x) or b[2]==a[2]+y)):
                print(2)
                temp=1
        if(temp==0 and a[2]!=a[1]):
            x=(((b[2]-b[1])*(1.0))/(a[2]-a[1]));
            y=(((b[1]*a[2])-(a[1]*b[2])*(1.0))/(a[2]-a[1]));
            if(x==int(x)  and  y==int(y)  and  (b[0]==((a[0]*x)+y) or b[0]==(a[0]*x) or b[0]==a[0]+y)):
                print(2)
                temp=1
        if(temp==0 and a[0]!=a[2]):
            x=(((b[0]-b[2])*(1.0))/(a[0]-a[2]));
            y=(((b[2]*a[0])-(a[2]*b[0])*(1.0))/(a[0]-a[2]));
            if(x==int(x)  and  y==int(y)  and  (b[1]==((a[1]*x)+y) or b[1]==(a[1]*x) or b[1]==a[1]+y)):
                print(2)
                temp=1
        if(temp==0  and  a[0]!=a[1]):
            x=(((b[1]*a[0])-(a[1]*b[0])*(1.0))/(b[0]-b[1]));
            y=(((b[0]-b[1])*(1.0))/(a[0]-a[1]));
            if(x==int(x)  and  y==int(y)  and  (b[2]==((a[2]+x)*y) or b[2]==(a[2]+x) or b[2]==a[2]*y)):
                print(2)
                temp=1
        if(temp==0  and  a[0]!=a[2]):
            x=(((b[2]*a[0])-(a[2]*b[0])*(1.0))/(b[0]-b[2]));
            y=(((b[0]-b[2])*(1.0))/(a[0]-a[2]));
            if(x==int(x)  and  y==int(y)  and  (b[1]==((a[1]+x)*y) or b[1]==(a[1]+x) or b[1]==a[1]*y)):
                print(2)
                temp=1
        if(temp==0  and  a[2]!=a[1]):
            x=(((b[1]*a[2])-(a[1]*b[2])*(1.0))/(b[2]-b[1]));
            y=(((b[2]-b[1])*(1.0))/(a[2]-a[1]));
            if(x==int(x)  and  y==int(y)  and  (b[0]==((a[0]+x)*y) or b[0]==(a[0]+x) or b[0]==a[0]*y)):
                print(2)
                temp=1
        if(temp==0):
            print(3)
except:
    pass
