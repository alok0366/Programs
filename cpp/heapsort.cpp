#include<iostream>
using namespace std;
void max_heapify(int a[],int i,int n){
    int left=2*i;
    int right=(2*i+1);
    int largest;
        if((left<=n) && a[left]>a[i])
            largest=left;
            else
                largest=i;
            if((right<=n) && a[right]>a[i])
                largest=right;
            if(largest!=i){
                swap(a[i],a[largest]);
            max_heapify(a,largest,n);}
        }
void build_max_heap(int a[], int n)
{
  for(int k = n/2; k >= 1; k--)
    {
      max_heapify(a, k, n);
    }
}
void HEAPSORT(int a[], int n)
{

  build_max_heap(a,n);
  int i, temp;
  for (i = n; i >= 2; i--)
    {
      temp = a[i];
      a[i] = a[1];
      a[1] = temp;
      max_heapify(a, 1, i - 1);
    }
}

int main()
{
  int n;
  cout<<"Enter the size of the array"<<endl;

        int a[n];
    cout<<"how many elemnent u want to enter"<<endl;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>a[i];
    cout<<"elements after sorting:"<<endl;
    HEAPSORT(a,n);
    for(int i=0;i<n;i++)
        cout<<a[i]<<"";
    }
