try:
    s=input()
    s1=""
    for i in s:
        if i.isalpha():
            s1+=i
        elif i.isnumeric():
            s1+=i
    s1=s1.upper()
    print(s1,s1[::-1])
    if s1==s1[::-1]:
        print(1)
    else:
        print(0)
except EOFError as e:
    print(e)
