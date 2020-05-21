#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    ll t;
    cin>>t;
    while(t--){
        ll N,Q;
        string s;
        cin>>N>>Q>>s;
        set<char>ss;
        for(ll p:s){
            ss.insert(p);
        }
        vector<int>freq;
        for(char c:ss){
                ll cc=0;
            for(char a:s){
                if(a==c){
                    cc++;
                }
            }
            freq.push_back(cc);
        }
        ll x;
        for(int i=0;i<Q;i++){
                cin>>x;
                ll ans=0;
                for(auto p:freq){
                    if(p>x){
                        ans+=p-x;
                    }
                }
                cout<<ans<<"\n";
        }
    }
    return 0;
}
