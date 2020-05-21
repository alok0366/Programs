/*mahendra25---PVPSIT-IT
IT ONLY HAS TO WORK ONCE!
*/
#include<bits/stdc++.h>
using namespace std;
#define pi 3.14159265358979323846264338327950
const int N=1e6+20,mod=(int)(1e9)+7;
#define ONLINE_JUDEGE
#define pb push_back
#define ull unsigned long long
#define ll long long
int main(){
   #ifdef ONLINE_JUDEGE
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   #endif
   int T;
   scanf("%d",&T);
   while(T--){
    	ll num;
    	cin>>num;
    	ll ans=(ll)floor(num/2);
    	if(num%2)
    		cout<<ans-1<<endl;
    	else
    		cout<<ans<<endl;
   }
  return(0);
}
