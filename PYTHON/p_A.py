try:
    n=int(input())
    st=input()
    fans=""
    for i in range(n):
        if len(fans)%2==0 or fans[-1]!=st[i]:
            fans+=st[i]
    if len(fans)%2!=0:
        fans=fans[:-1]
    print(n-len(fans))
    print(fans)
except:
    pass
