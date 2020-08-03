import sys
def binary_search(lw,hi): 
    low = lw
    high =hi
    mid = 0
    print(n)
    while low <= high: 
        mid = (high + low) // 2
        print(mid)
        ans=input()
        if ans=="E":
            return mid
        elif ans=="G":
            low=mid+1
            ans=""
            while(ans!="G"):
                print(n)
                ans=input()
                if ans=="E":
                    sys.exit(0)
        elif ans=="L":
            high=mid-1
            ans=""
            while(ans!="G"):
                print(n)
                ans=input()
                if ans=="E":
                    sys.exit(0)
  
    return -1


def b_s(low,high):
    start=low
    end=high
    mid=(start+end)//2
    print(mid)
    ans=input()
    if ans=="E":
        sys.exit(0)
    elif ans=="L":
        x=(mid+end)//2
        print(x)
        ans=input()
        if ans=="E":
            sys.exit(0)
        elif ans=="L":
            b_s(start,x)
        else:
            b_s(start,mid-1)
            b_s(mid+1,end)
    else:
        x=(start+mid)//2
        print(x)
        ans=input()
        if ans=="E":
            sys.exit(0)
        elif ans=="G":
            b_s(x,end)
        else:
            b_s(start,mid-1)
            b_s(mid+1,end)
        
        

try:
    n=int(input())
    if n!=100000 or n!=10**9:
        ans=""
        while(ans!="G"):
            print(n)
            ans=input()
            if ans=="E":
                sys.exit(0)
        binary_search(1,n)
    else:
        start=1
        end=n
        b_s(start,end)
except:
    pass
        
