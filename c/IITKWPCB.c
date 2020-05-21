#include<iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        long long x;
        cin>>x;
        long long ans=(long long)floor(x/2);
        if(num%2)
            cout<<ans-1<<endl;
        else
            cout<<ans<<endl;
        }
    return 0;
    }
