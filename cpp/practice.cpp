#include<iostream>
#include<string.h>
using namespace std;
int main(){
    char a[30];
   string rev;
    cout<<"enter any string:\n";
    cin.getline(a,30);
    string k=a;
    rev=strrev(a);
    cout<<k<<" "<<rev;
    }
