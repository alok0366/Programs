#include<iostream>
#include<list>
using namespace std;
void display(list<double>&lst){
    list<double>::iterator p;
    for(p=lst.begin();p!=lst.end();p++)
        cout<<*p<<" ";
        cout<<"\n\n";
    }
int main(){
    double x;
    list<double>lst;
    cout<<"ENTER 3 ELEMENTS TO ADD AT BACK:"<<endl;
    for(int i=0;i<3;i++){
        cin>>x;
        lst.push_back(x);}
        display(lst);
        cout<<"ENTER 4 ELEMENTS TO INSRT AT FORNT:"<<endl;
        for(int i=0;i<4;i++){
            cin>>x;
            lst.push_front(x);}
            display(lst);
            cout<<"FIRST AND LAST ELEMENTS OF THE LIST IS:"<<endl;
            list<double>::iterator p=lst.begin();
            cout<<"FIRST : "<<lst.front()<<endl;

            cout<<"LAST : "<<lst.back()<<endl;
            display(lst);
                cout<<"DELTEING THE FIRST AND LAST ELEMENT : "<<endl;
            lst.pop_front();
            lst.pop_back();
            display(lst);

            cout<<"AT WHICH POS U WANT TO INSERT ELEMENT:"<<endl;
            cin>>x;
            p=lst.begin();
            for(int i=0;i<x;i++)
                p++;
            cout<<"ENTER THE ELEMENTS:"<<endl;
            cin>>x;
            lst.insert(p,x);
                display(lst);
             cout<<"AT WHICH POS U WANT TO DELETE ELEMENT:"<<endl;
            cin>>x;
            p=lst.begin();
            for(int i=0;i<x;i++)
                p++;
            lst.erase(p);
            display(lst);
            lst.sort();
                cout<<"SORTED LIST : ";
            display(lst);
            list<double>lst2;
            cout<<"ENTER 5 ELEMENTS IN THE LIST 2"<<endl;
            for(int i=0;i<5;i++){
                cin>>x;
            lst2.push_back(x);}
            lst2.merge(lst);
            display(lst2);
            return 0;
}



