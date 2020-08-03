import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for t in range(1,int(input())+1):
    n=int(input())
    s=input()
    print(s)
    A=s.count("A")
    B=s.count("B")
    if abs(A-B)==1:
        ans="Y"
    else:
        ans="N"
    print("Case #{}:".format(t),ans)
print("alok")
