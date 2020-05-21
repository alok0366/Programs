#include<iostream>
#include<vector>
//#include<string.h>
using namespace std;
void display(vector<string>v){
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<" ";
    }
int main(){
    string str;
    vector<string>v;
    cout<<"ENTER 8 STRINGS"<<endl;
    for(int i=0;i<8;i++){
    getline(cin,str);
    v.push_back(str);}
    display(v);
    vector<string>::iterator itr=v.begin();
    cout<<"\nENTER TWO MORE STRINGS TO BE INSERTED IN THE VECTOR ARRAY AT POS 3 AND 6:"<<endl;
        getline(cin,str);
        v.insert(v.begin()+3,str);
        getline(cin,str);
        v.insert(v.begin()+6,str);
        display(v);
        cout<<"\nDELETING ELEMENTS FROM POS 2 TO 5 "<<endl;
        //v.erase(v.begin()+2,v.begin()+5);

        v.insert(v.begin()+2,"anand");
        display(v);
        cout<<"\nNOW ENTER STRINGS TO ATTATCH IN  VECTOR FROM POS 2 TO 5"<<endl;
        for(int i=2;i<6;i++){
            getline(cin,str);
            v.insert(v.begin()+i,str);}
            display(v);
            cout<<"\nNOW FIRST AND LAST STRINGS ARE"<<endl;
            cout<<v[0]<<endl<<v[v.size()-1]<<endl;
            cout<<"SIZE OF THE VECTOR :"<<v.size()<<endl;
            display(v);
            return 0;
}




