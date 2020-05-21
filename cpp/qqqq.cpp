#include<iostream>
using namespace std;
int main(){
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    cout<<"Before try \n";
    try{
        cout<<"inside try\n";
        if(num<0){
            throw num;
            cout<<"after throw is executed\n";

        }
        cout<<"non negative no";
    }
    catch(int n){
        cout<<"exception caught:negatiev\n";
}
cout<<"after catch is execiyed";
return 0;
}
