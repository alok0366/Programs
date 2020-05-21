#include<stdio.h>
#include<iostream>
using namespace std;
 void mergesort(int a[],int i,int j);
    void merge(int a[],int i1,int j1,int i2,int);
int main(){
    cout<<"enter the no of elements"<<endl;
    int a[30],n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>a[i];
    cout<<"entered elements are :"<<endl;
    for(int i=0;i<n;i++)
        cout<<a[i];
        mergesort(a,0,n-1);
        printf("\nSorted array is :");
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);
        return 0;
    }
    void mergesort(int a[],int i,int j){
        if(i<j){
            int mid;
            mid=(i+j)/2;
            mergesort(a,i,mid);
            mergesort(a,mid+1,j);
            cout<<"\ni="<<i<<"\nj="<<j<<"\nmid="<<mid;
            merge(a,i,mid,mid+1,j);
        }}
   void merge(int a[],int i1,int j1,int i2,int j2)
{
    int temp[50];    //array used for merging
    int i,j,k;
    i=i1;    //beginning of the first list
    j=i2;    //beginning of the second list
    k=0;

    while(i<=j1 && j<=j2)    //while elements in both lists
    {
        if(a[i]<a[j])
            temp[k++]=a[i++];
        else
            temp[k++]=a[j++];
    }

    while(i<=j1)    //copy remaining elements of the first list
        temp[k++]=a[i++];

    while(j<=j2)    //copy remaining elements of the second list
        temp[k++]=a[j++];

    //Transfer elements from temp[] back to a[]
    for(i=i1,j=0;i<=j2;i++,j++)
        a[i]=temp[j];
}

