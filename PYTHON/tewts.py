""" using counters as well as most_common() and x.items() methos also"""


from collections import Counter as c
try:
    arr=[int(i) for i in input().split()]
    cc=c(arr)
    cc=cc.items()
    print(cc)
    for ele,c in cc:
        print(ele,c)
except:
    pass
