import math
try:
    for _ in range(int(input())):
        n=int(input())
        if n%2!=0:
            if n==1:
                print("FastestFinger")
            else:
                print("Ashishgup")
        else:
            div=0
            for i in range(3,n+1,2):
                if n%i==0:
                    div=i
                    break
            if div==0:
                n=n-1
                if n==1:
                    print("Ashishgup")
                else:
                    print("FastestFinger")
            else:
                c2=1
                while(n!=1):
                    if n%2==0:
                        if n%div==0:
                            n=n//div
                            c2=1-c2
                        else:
                            n=n-1
                            c2=1-c2
                    else:
                        n=n//n
                        c2=1-c2
                if c2:
                    print("FastestFinger")
                else:
                    print("Ashishgup")
                        
            
            




        

except:
    pass
