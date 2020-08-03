try:
    for _ in range(int(input())):
        ts=int(input())
        if ts%2!=0:
            print((ts-1)//2)
        else:
            while(ts%2==0):
                ts=ts>>1
            print((ts-1)//2)
                
except:
    pass
