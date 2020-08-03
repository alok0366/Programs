def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return Tru
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

try:
    for _ in range(int(input())):
        n,k=map(int,input().split())
        if k<n:
            if k==1:
                print(1)
            elif k==2:
                if(isPrime(n)):
                    print(0)
                else:
                    print(1)
            elif k>2:
                
        else:
            print(0)
except:
    pass
                
