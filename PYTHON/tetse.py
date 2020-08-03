# cook your dish here
import math
import sys
import heapq
from collections import Counter
def solve(strr):
    marks=0
    l=len(strr)
    if l==7 and strr=="ACov(A)" or strr=="BCov(B)" or strr=="CCov(C)" or strr=="DCov(D)" or strr=="ECov(E)" or strr=="FCov(F)":
            marks=1
            return marks
    else:
        pre=["ACov","BCov","CCov","DCov","ECov","FCov"]
        for i in pre:
            if i in strr:
                marks=0.5
                return marks
        post=["(A)","(B)","(C)","(D)","(E)","(F)"]
        for i in post:
            if i in strr:
                marks=0.5
                return marks
    return marks
                
try:
    gnome=[];x=0
    while True and x<6:
        s=input()
        if not s:
            break
        else:
            gnome.append(s)
            x+=1
    ans=0
    for i in gnome:
        ans+=solve(i)
    print(ans,"out of 6")
    
        
        
                
        
        
except:
    pass
