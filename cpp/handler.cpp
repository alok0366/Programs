#include<iostream>
using namespace std;
void handler(int);
int main(){
    cout<<"enter a no"<<endl;
    int y;
    cin>>y;
    handler(y);
    return 0;
    }
   void handler(int x){
        try{
        if(x>0 && x%2==0)
            throw 5;
        if(x>0 && x%2!=0)
            throw 'a';
        if(x<0)
           throw "abc";}

        catch(int x){
        cout<<"even";
        }
        catch(char c){
        cout<<"odd";
        }
        catch(...){
        cout<<"negative no";}

    }

