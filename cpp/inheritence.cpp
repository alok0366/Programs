#include<iostream>
using namespace std;
class a{
    char name[20];
    int id;
public:
    void seta(){
        cout<<"enter the name and id of the student"<<endl;
        cin>>name>>id;}
        void disa(){
            cout<<name<<id;}
    };
class b{
    float salary;
    public:
    void setb(){
    cout<<"enter the salary of the student"<<endl;
    cin>>salary;}
    void disb(){
        cout<<salary;}
    };
class c{
    char sec[20];
    public:
    void setc(){
        cout<<"enter the sec of the student:"<<endl;
        cin>>sec;}
        void disc(){
        cout<<sec;}
    };
class d:public a,public b,public c{
};
int main(){
    d obj;
    obj.seta();obj.setb();obj.setc();
    obj.disa();obj.disb();obj.disc();
    return 0;
    }
