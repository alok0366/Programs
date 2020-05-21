#include<iostream>
using namespace std;
int fi(int n) {
int result = n;
for(int i=2;i*i <= n;i++) {
if (n % i == 0) result -= result / i;
while (n % i == 0) n /= i;
}
if (n > 1) result -= result / n;
return result;
}
int main(){
	int t,n,k;
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(0);
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		k=fi(n);
		cout<<k<<'\n';
	}
	return 0;
}
