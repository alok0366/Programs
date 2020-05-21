#include<iostream>
using namespace std;
 class students{
     char name[20];
     int roll;
     char dept[20];
 public:
    void create(){
        cout<<"ENTER NAME ,ROLL AND DEPT OF THE STUDENT:"<<endl;
        cin>>name>>roll>>dept;}
       void display(){
       cout<<"NAME:"<<name<<endl<<"ROLL:"<<roll<<endl<<"DEPT:"<<dept<<endl;}
    };
 class marks:public students{
    int marks;
public:
    void setmarks(){
        cout<<"ENTER THE MARKS:"<<endl;
        cin>>marks;}
        void display1(){
            display();
          cout<<"MARKS:"<<marks<<endl;}
    };
int main(){
    marks obj[20];
    cout<<"HOW MANY STUDENTS DATA U WANT TO ENTER:?"<<endl;
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        obj[i].create();
        obj[i].setmarks();
    }
    A:
    for(int i=0;i<n;i++){
        obj[i].display1();
    }
    cout<<"DO U WANNA UPdATE SOMETHING IN THE LIST:ENTER 0 OR 1"<<endl;
    int ch;
    cin>>ch;
    if(ch){
        cout<<"FOR WHICH NO STUDENT U WANT TO UPDATE:"<<endl;
        int j;
        cin>>j;
        obj[j].create();
        obj[j].setmarks();
        goto A;}
    return 0;
    }
