def bubblesort(arr,n):
    c=0
    l=n
    swap=True
    while(swap!=False):
        swap=False
        c+=1
        for i in range(l-2):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swap=True
    return c




try:
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(bubblesort(arr,n))
except:
    pass
