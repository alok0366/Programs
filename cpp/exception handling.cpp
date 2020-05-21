#include<iostream>
using namespace std;
void handler(int test)throw(int,char,double){
    if(test==0)throw 5;
        if(test==1)throw 1;
            if(test==2)throw 2;
                if(test==3)throw 3;
}
int main(){
    try{
        handler(0);
        handler(2);
        handler(3);
        }
        catch(int i){
        cout<<"exeptipoon cauht"<<i<<endl;
        }
        return 0;
}
