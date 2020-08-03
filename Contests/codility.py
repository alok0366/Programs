def solution(H):
    stack1=[]
    stack2=[]
    n=len(H)
    mx=max(H)
    for i in range(n):
        if H[i]==mx:
            break
        else:
            stack1.append((H[i]))
    for i in range(n-1,-1,-1):
        if H[i]==mx:
            break
        else:
            stack2.append((H[i]))
    l1=len(stack1)
    l2=len(stack2)
    if l1 and l2:
        m1=max(stack1)
        m2=max(stack2)
        if m1==m2:
            if l1>l2:
                return (mx*(n-l1)+m1*l1)
            else:
                return (mx*(n-l2)+m2*l2)
        else:
            if m1>m2:
                return (mx*(n-l2)+m2*l2)
            else:
                return (mx*(n-l1)+m1*l1)
    elif l1:
        m1=max(stack1)
        return (mx*(n-l1)+m1*l1)
    elif l2:
        m2=max(stack2)
        return (mx*(n-l2)+m2*l2)
    else:
        return (mx*n)
            
            
            
try:
    st=input()
    H=[]
    print(st)
    for i in st:
        if i.isnumeric():
            H.append(int(i))
    print(H)
    sol=solution(H)
    print(sol)
except:
    pass
            
            
            
            
