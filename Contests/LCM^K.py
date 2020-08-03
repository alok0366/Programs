def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 

def pw(a,b,c):
    ans=1
    a=a%c
    if a==0:
        return 0
    while(b>0):
        if(b&1):
            ans=(ans*a)%c
        b=b>>1
        a=(a*a)%c
    return ans

try:
    for _ in range(int(input())):
        n,m,k=map(int,input().split())
        arr = [int(i) for i in input().split()]
        num1 = arr[0] 
        num2 = arr[1] 
        lcm = find_lcm(num1, num2) 
        for i in range(2, len(arr)): 
            lcm = find_lcm(lcm, arr[i])
        lcm=pw(lcm,k,m)
        print(lcm%m)
  

except:
    pass





















        
        
