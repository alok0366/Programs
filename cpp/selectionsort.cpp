#include<iostream>
void selectionsort(int a[],int);
using namespace std;
int main(){
    int n;
    cout<<"No of element u want to enter"<<endl;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
        cin>>a[i];
        selectionsort(a,n);
        for(int i=0;i<n;i++)
            cout<<endl<<a[i]<<""<<endl;
        return 0;
    }
    void selectionsort(int a[],int n){
    for(int j=0;j<n;j++){
    for(int i=0;i<n;i++){
        if(a[j]<a[i]){
            swap(a[j],a[i]);
            }
            }
    }}

