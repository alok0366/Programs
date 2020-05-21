#include<iostream>
#include<stdio.h>
using namespace std;
long long int gcd(long long int c,long long int d){
    if(d==0)
        return c;
    else
        return gcd(d,c%d);
        }
int main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int n,m;
    long long int c=1,d=1;
    long long int ans=1;
    cin>>n;
    int arn[n];
    for(int i=0;i<n;i++){
        cin>>arn[i];}
    cin>>m;
    int arm[m];
    for(int i=0;i<m;i++){
        cin>>arm[i];}

        for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            ans*=gcd(arn[i],arm[j]);
            if(ans>1000000000) fl=1;
            ans=ans%1000000000;
        }
    }
        if(ans<1000000000){
            cout<<c<<'\n'<<d<<'\n'<<ans;
        }
        else{
            int r=0,rem=0,ansf[9];
                while(ans!=0 && r!=9){
                    rem=ans%10;
                    ansf[r]=rem;
                    ans=ans/10;
                    r++;
                }
        for(int i=8;i>=0;i--){
            cout<<ansf[i];
        }}
        return 0;}

