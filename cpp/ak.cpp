#include<iostream>
using namespace std;

int main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);
    long long int i;
    long long int x;
    cin>>x;
    long long int arr[x];
    for( i =0; i<x;i++)
        cin>>arr[i];
    long long int max=0;
    for( i =0; i<x;i++){
        if(arr[i]>max)
            max=arr[i];
    }
    long long int arri[max+1];
    for( i =0; i<x;i++){
        if(arri[arr[i]]!=1){
            cout<<"NO"<<endl;
            arri[arr[i]]=1;
        }
        else
            cout<<"YES"<<endl;
    }

}
