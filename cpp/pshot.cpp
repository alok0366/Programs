#include<bits/stdc++.h>
#include<string.h>
#define ll long long
using namespace std;
int main(){
    ll t,n,a=0,b=0;
    string str;
    cin>>t;
    while(t--){
        cin>>n;
        cin>>str;
        for(int i=1;i<=n;i+=2){
            a=a+str[i]-'0';
            b=b+str[i-1]-'0';
            ll c=a-b;
            if(c>=2*n-i){
                cout<<i<<endl;
                break;
            }
        }

    }
    }
