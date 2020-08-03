t=int(input())
while(t):
    t-=1;flag=0;count=0;n=int(input())
    while(n!=1):
        if((n and (n-1))==0):print(-1);flag=1; break;
        elif(n%6==0):n=n//6
        else:n*=2;
        count+=1;
    if(flag==0):print(count)
