#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
int N;
cin>>N;
for(ll y=1;y<=N;y++){
ll n,x,flag=0;
cin>>n>>x;
if(((n*(n+1))/2)==x && n!=2){
      cout<<"Case #"<<y<<": "<<"POSSIBLE\n";
flag=1;
for(ll i=1;i<=n;i++){
cout<<i<<" ";
ll j=i+1;
while(j!=i && i!=n){
cout<<j<<" ";
j++;
if(j>n) j=1;
}
if(i==n){
for(ll k=1;k<=n-1;k++) cout<<k<<" ";
}
cout<<endl;
}
}
//ll m;
for(int i=1;i<=n;i++){
if(n*i==x && flag==0){
cout<<"Case #"<<y<<": "<<"POSSIBLE\n";
for(ll l=i;l>0;l--){
//for(ll m=1;m<i;m++){
cout<<l<<" ";
ll j=l+1;
while(j!=l && l!=n){
cout<<j<<" ";
j++;
if(j>n) j=1;
}
if(l==n){
for(ll k=1;k<=n-1;k++) cout<<k<<" ";
}
cout<<endl;
}
for(ll l=n;l>i;l--){
cout<<l<<" ";
ll j=l+1;
while(j!=l && l!=n){
cout<<j<<" ";
j++;
if(j>n) j=1;
}
if(l==n){
for(ll k=1;k<=n-1;k++) cout<<k<<" ";
}
cout<<endl;
}
flag=1;
}
}
if(flag==0) cout<<"Case #"<<y<<": "<<"IMPOSSIBLE\n";
}
}

