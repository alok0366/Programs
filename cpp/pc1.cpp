#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
int main(){
    string str;
    int k=0,l,m;
    cout<<"ENTER THE TEXT : ";
    getline(cin,str);
    cout<<endl<<endl;
    int c=str.length();
    for(int j=0;j<c;j++){
    for(int i=j;i<c;i++){
        if(j==0){
        cout<<str[i]<<" ";}
        else if(j==c-1){
            cout<<str[c-i-1]<<" ";}

        else{
            cout<<str[i+1]<<endl;
        }}

    cout<<endl;}
    return 0;
}

