#include <iostream>
using namespace std;

int main() {
    long long int T,count1=0,count2=0,c=0;
    cin>>T;
    long long int N,A,B,K;
    for(int i=1;i<=T;i++){
        cin>>N>>A>>B>>K;
        for(int i=1;i<=N;i++){
            if(i%A==0 && i%B==0)
                count1++;
            if(i%A!=0 && i%B!=0)
                count2++;
        }
        c=N-(count1+count2);
        if(c>=K)
            cout<<"win";
            else
            cout<<"lose";
    }
	return 0;
}
