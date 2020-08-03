import sys
def b_s(low,high):
    while(low<=high):
        mid=(low+high)//2
        print(1)
        a_1=input()
        print(mid)
        f_1=input()
        if f_1=="E":
            sys.exit(0)
        print(n)
        a_2=input()
        print(mid)
        f_2=input()
        if f_2=="E":
            sys.exit(0)
        if a_1=="L":
            if f_1=="G":
                b_s(mid+1,high)
            else:
                b_s(low,mid-1)
        elif a_2=="G":
            if f_2=="G":
                b_s(mid+1,high)
            else:
                b_s(mid+1,high)
        else:
            if f_1=="L" and f_2=="L":
                b_s(low,mid-1)
            elif f_1=="G" and f_2=="G":
                b_s(mid+1,high)
        
        

try:
    n=int(input())
    print(n)
    ans=input()
    if ans=="E":
        sys.exit(0)
    print(1)
    ans=input()
    if ans=="E":
        sys.exit(0)
    b_s(2,n-1)
except:
    pass
        
