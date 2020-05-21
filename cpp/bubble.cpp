#include<iostream>
template<class T>
void bubblesort(T a[],int);
using namespace std;
int main(){
    int n;
    int a[5]={56,34,45,23,12};
    float b[5]={1.23,5.65,23.45,0.65,7.3};
    //cout<<"how many no u want to enter "<<endl;
    //cin>>n;
    //for(int i=0;i<n;i++)
      //  cin>>a[i];
   bubblesort(a,5);
    bubblesort(b,5);
        return 0;
    }
template<class T>
void bubblesort(T a[],int n){
    int i,j;
    for(j=0;j<6;j++){
    for(i=0;i<6;i++){
        if(a[i]>a[i+1]){
            swap(a[i],a[i+1]);

    }

    }}
    for(int i=0;i<5;i++)
        cout<<a[i]<<""<<endl;

}
