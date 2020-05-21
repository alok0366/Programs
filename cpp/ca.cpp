#include <iostream>
#include<string.h>
using namespace std;
void ca(int r,int c){
    int m=0;
    string str="*.";
	for(int j=0;j<r;j++){
            m=j%2;
	for(int i=0;i<c;i++){
	cout<<str[m%2];
	m++;}
	cout<<endl;
	}
}

int main() {
	int n,r,c;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>r>>c;
		ca(r,c);
	}
	return 0;
	}
