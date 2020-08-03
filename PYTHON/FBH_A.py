try:
    for _ in range(int(input())):
        n=int(input())
        I=input()
        O=input()
        flg=0
        ans=[]
        for i in range(n):
            tem=[0]*n
            tem[i]="Y"
            ptr=i+1
            flg=1
            while(ptr<n):
                if O[ptr-1]=="Y" and I[ptr]=="Y" and flg:
                    tem[ptr]="Y"
                else:
                    flg=0
                    tem[ptr]="N"
                ptr+=1
            ptr=i-1
            flg=1
            while(ptr>-1):
                if O[ptr+1]=="Y" and I[ptr]=="Y" and flg:
                    tem[ptr]="Y"
                else:
                    tem[ptr]="N"
                    flg=0
                ptr-=1
            ans.append(tem)
        print("Case #{}:".format(_+1))
        for i in range(n):
            for j in range(n):
                print(ans[i][j],end="")
            print()
except:
    pass
