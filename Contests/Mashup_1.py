import math
from collections import Counter
try:
    for _ in range(1):
        s=input()
        s=list(s.split("|"))
        x=input()
        #print(s,x)
        ptr=0
        while(ptr<len(x)):
            if len(s[0])<len(s[1]):
                s[0]+=x[ptr]
                ptr+=1
            else:
                s[1]+=x[ptr]
                ptr+=1
        if len(s[0])!=len(s[1]):
            print("Impossible")
        else:
            print(s[0]+'|'+s[1])
        
except:
    pass
