import math
try:
    for _ in range(int(input())):
        n=int(input())
        if n%2!=0:
            n=n-1
        print(math.gcd(n,n//2))
            
            




        

except:
    pass
