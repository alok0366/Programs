try:
    for _ in range(int(input())):
        s=input()
        l=len(s)
        if l>10:
            print(s[0]+str(l-2)+s[l-1])
        else:
            print(s)
except:
    pass
