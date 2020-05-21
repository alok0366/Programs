#include<stdio.h>
#include<iostream>
using namespace std;
int main(){
    //int num;
    void fun(int);
    //cout<<"entre the no";
    //cin>>num;
    fun(1);
    return 0;
    }
void fun(int num) { int freq[11], denom[11]={ 2000,1000,500,200,100,50,20,10,5,2,1}; for(int i = 0; i <=10; i++) { freq[i] = num / denom[i]; if(freq[i] != 0) num = num - freq[i] * denom[i]; } for(int i = 0; i <= 10; i++) cout<<denom[i]<<" \t- \t"<<freq[i]<<endl;}
