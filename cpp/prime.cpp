#include<iostream>
using namespace std;
int main(){
    int n,i,j;
    int count=0;
    cout<<"upto what no prime no u want";
    cin>>n;
    for(i=1;i<n;i++){
    for(j=1;j<i;j++){
        count=0;
        if(i%j==0)
        count++;
        if(count==1)
        break;
        else
            cout<<j;}
        }

    }
