#include<iostream>
using namespace std;
template<class x>
void Binary_Search(x a[],int i,int j,x no){
    x mid;
    x n=no;
    int s=i;
    int f=j;
    mid=(s+f)/2;
    if(a[mid]==n)
        cout<<"NO IS PRESENT IN THE ARRAY AT THE INDEX:"<<mid<<endl;

    if(n>a[mid]){
            s=mid+1;
        Binary_Search(a,s,f,no);}
    if(n<a[mid]){
        f=mid;
        Binary_Search(a,s,f,no);
    }
}
int main(){
    cout<<"HOW MANY NO U WANT TO ENTER:?"<<endl;
    int n,s;
    cin>>n;
    int a[n];
    cout<<"ENTER THE VALUE OF THE ARRAY IN THE ASCENDING ORDER:"<<endl;
    for(int i=0;i<n;i++)
        cin>>a[i];
        cout<<"WHICH NO U WANT TO SEARCH IN THE ARRAY?"<<endl;
        cin>>s;
        Binary_Search(a,0,n,s);
        return 0;

    }




