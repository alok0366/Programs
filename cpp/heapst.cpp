#include<iostream>
using namespace std;
void heapst(int a[],int,int);
void maxheapify(int a[],int,int);
int main(){
    int n;
    cout<<"enter the size of the array";
    cin>>n;
    int a[n+1];
    cout<<"enter the elemesnts of ths array:";
    for(int i=1;i<=n;i++)
    cin>>a[i];
    int i=n/2;
    heapst(a,i,n);
    for(int i=1;i<=n;i++)
        cout<<a[i];
    }
    void heapst(int a[],int i,int n){
        for(int k=i;k>=1;k--){
        maxheapify(a,i,n);}
        int temp;
        temp=a[1];
        a[1]=a[n];
        a[n]=temp;n--;
        if(i>1){
                int i=n/2;
        heapst(a,i,n-1);
        }}
void maxheapify(int a[], int i, int n)
{
  int l,r,largest,loc;
  l=2*i;
  r=(2*i+1);
  if((l<=n)&&a[l]>a[i])
    largest=l;
  else
    largest=i;
  if((r<=n)&&(a[r]>a[largest]))
    largest=r;
  if(largest!=i)
    {
      loc=a[i];
      a[i]=a[largest];
      a[largest]=loc;
    }
}
