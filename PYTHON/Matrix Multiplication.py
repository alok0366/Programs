try:
    print("Enter the row and column of matrix of First matrix and then Second matrix")
    r1,c1,r2,c2=map(int,input().split())
    if c1!=r2:
        print("Matrix Multiplication is not possible")
    else:
        print("Enter the details of first matrix")
        M1=[];M2=[]
        for i in range(r1):
            tem=[int(i) for i in input().split()]
            M1.append(tem)
        print("Enter the details of second matrix")
        for i in range(r2):
            tem=[int(i) for i in input().split()]
            M2.append(tem)
        print("Matrix Multiplication :-")
        ans=[[0]*c2 for i in range(r1)]
        for i in range(r1):
            for j in range(c2):
                sm=0
                for k in range(r2):
                    sm+=M1[i][k]*M2[k][j]
                ans[i][j]=sm
        for i in range(len(ans)):
            print(*ans[i])
except:
    pass
            
            
    
