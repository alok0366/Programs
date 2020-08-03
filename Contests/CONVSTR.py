t=int(input())
for test in range(t):
    n=int(input())
    A=input("")
    B=input("")
    index=dict()
    differ=dict()
    for i in range(n):
        if A[i] not in index.keys():
            index[A[i]]=i
    flag=0
    for i in range(n):
        if B[i]>A[i] or (B[i]!=A[i] and B[i] not in index.keys()):
            flag=1
            break
        elif A[i]!=B[i]:
            differ[B[i]]=differ.get(B[i],[])+[i]
    if flag==1:
        print(-1)
        continue
    value=sorted(list(differ.keys()),reverse=True)
    print(len(value))
    for i in value:
        temp=differ[i]+[index[i]]
        print(len(temp),*temp)
