def check(row,column):
    count=0
    while(row and column):
        if row>=column:
            row=row-column
        else:
            column=column-row
        count+=1
    return count


try:
    mn_l=int(input())
    mx_l=int(input())
    mn_w=int(input())
    mx_w=int(input())
    ans=0
    for i in range(mn_l,mx_l+1):
        for j in range(mn_w,mx_w+1):
            ans+=check(i,j)
    print(ans,end="")
except:
    pass
            
    
