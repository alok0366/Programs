import sys
import math
from collections import Counter
import heapq
def subarrayBitwiseOR(A):
    res=set()
    pre={0}
    for i in A:
        pre={i|j for j in pre}|{i}
        res.update(pre)
    return len(res)
try:
    for _ in range(int(input())):
        arr=[int(i) for i in input().split()]
        print(subarrayBitwiseOR(arr))
except EOFError as e:
    print(e)
