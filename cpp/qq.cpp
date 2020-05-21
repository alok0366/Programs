#include<iostream>
#include<string.h>
using namespace std;
int main(){
    int i;
    char *str="c++";
    char *str2="programming";
    int m=strlen(str);
    int n=strlen(str2);
    for(i=1;i<n;i++){
        cout.write(str2,i);
        cout<<endl;
        }
        for(i=n;i>0;i--){
        cout.write(str2,i);
        cout<<endl;
        }
        cout.write(str,m).write(str2,n);
        cout<<endl;
        cout.write(str2,5);
        return 0;
        }
