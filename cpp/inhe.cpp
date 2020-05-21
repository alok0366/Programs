#include<iostream>
using namespace std;
class A{
    int a;
public:
    void seta(int x){
        a=x;
        }
    int geta(){
        return a;
        }

};
class B:private A{
    int b,c;
public:
    void setab(){
        int x,y;
        cout<<"ENTER A AND B :\n";
        cin>>x>>y;
        seta(x);
        b=y;
        }

        void diff(){

           c=geta();
        int d;
        d=c-b;
        cout<<d;}
    };
int main(){
    B b;
    b.setab();
    b.diff();
    return 0;
    }
