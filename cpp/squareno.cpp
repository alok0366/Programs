#include<bits/stdc++.h>
#include<vector>
#define ll long long int
using namespace std;
int main(){
    ll t,n,x,c,mul=1;
    string m;
    vector<ll>v;
    cin>>t;
    while(t--){
        c=0;
            cin>>n;
    for(int i=0;i<n;i++){
        cin>>x;
        v.push_back(x);}
    for(ll i=0;i<n;i++){
            mul=1;
        for(ll j=i;j<n;j++){
            mul=(mul*(v[j])%4)%4;
            if(mul%4!=2){
                c++;
            }
        }}
    cout<<c<<"\n";}
    return 0;
    }
