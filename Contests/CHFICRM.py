try:
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        c_m=0
        flg=0
        chg={5:0,10:0,15:0}
        if arr[0]==15 or arr[0]==10:
            print("NO")
        else:
            for i in range(n):
                if arr[i]-5<=c_m:
                    c_m+=arr[i]
                    chg[arr[i]]+=1
                    ret=arr[i]-5
                    if ret==0:
                        continue
                    else:
                        if ret==10:
                            if chg[10]>0:
                                c_m-=ret
                                chg[10]-=1
                            elif chg[5]>=2:
                                c_m-=ret
                                chg[5]-=2
                            else:
                                flg=1
                                break
                        else:
                            if chg[ret]>0:
                                c_m-=ret
                                chg[ret]-=1
                            else:
                                flg=1
                                break
                else:
                    flg=1
                    break
            if flg:
                print("NO")
            else:
                print("YES")          
except:
    pass
