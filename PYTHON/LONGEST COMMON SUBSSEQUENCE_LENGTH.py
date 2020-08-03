try:
    print("PROGRAM TO FIND LONGEST COMMON SUBSEQUENCE LENGTH")
    print("ENTER THE FIRST STRING")
    s1=input()
    l1=len(s1)+1
    print("ENTER THE SECOND STRING")
    s2=input()
    l2=len(s2)+1
    ans=[[0]*l2 for i in range(l1)]
    for i in range(1,l1):
        for j in range(1,l2):
            if s1[i-1]==s2[j-1]:
                ans[i][j]=ans[i-1][j-1]+1
            else:
                ans[i][j]=max(ans[i-1][j],ans[i][j-1])
    print("MAXIMUM COMMON SUBSEQUENCE LENGTH IS :",ans[-1][-1])
                
except EOFError as e:
    print(e)
