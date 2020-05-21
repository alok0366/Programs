#include<bits/stdc++.h>
using namespace std;
int main(){
    string strs,strr,x="1";
    int c_1=1;
    cout<<"ENTER THE DATA FOR EVEN PARITY"<<endl;
    cin>>strs;
    for(int i=0;i<strs.length();i++){
            if(strs[i]==1){
                c_1++;
            }
    }
    if(c_1%2!=0){
        strs=strs+x;
    }
    cout<<"SENT DATA WITH PARITY IS "<<strs<<endl;
    cout<<"NOW ENTER THE DATA WHICH IS REECIVED TO YOU"<<endl;
    cin>>strr;
    if(strs==strr){
        cout<<"NO ERRORS IN TRANSMISSION"<<endl;
    }
    else{
        cout<<"ERROR HAS OCCURED"<<endl;
    }

    return 0;
}









