//merge sort implementation
#include<bits/stdc++.h>
#define ll long long
using namespace std;
void merge(vector<ll>&arr,ll p,ll q,ll r){
    ll n1,n2;
    n1=q-p+1;
    n2=r-q;
    vector<ll>L(n1),R(n2);
    for(ll i=0;i<n1;i++){
        L[i]=arr[p+i];
    }
    for(ll i=0;i<n2;i++){
        R[i]=arr[q+i+1];
    }
    //L[n1]=INT_MAX; // To use this we can make L and R to be arr of size n1+1 and n2+1
    //R[n2]=INT_MAX;
    ll i=0,j=0;
    for(ll k=p;k<=r;k++){
        if(L[i]<=R[j]){
            arr[k]=L[i];
            i++;
        }
        else{
            arr[k]=R[j];
            j++;
        }
    }
}
void merge_sort(vector<ll>&arr,ll p ,ll r){
    if(p<r){
            int q;
            q=(p+r)/2;
        merge_sort(arr,p,q);
        merge_sort(arr,q+1,r);
        merge(arr,p,q,r);
    }
}
int main(){
    ll n;
    cout<<"how many data do u want to enter"<<endl;
    cin>>n;
    vector<ll>arr(n);
    for(ll i=0;i<n;i++){
            cin>>arr[i];
    }
    merge_sort(arr,0,n-1);
    for(ll i=0;i<arr.size();i++){
        cout<<arr[i]<<" ";

    }

}
