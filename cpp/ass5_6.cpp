#include<iostream>
#include<map>
#include<string.h>
using namespace std;
void display(map<int,string>&m){
    map<int,string>::iterator itr;
    for (itr = m.begin(); itr != m.end(); ++itr)
    {
        cout  <<  '\t' << itr->first
              <<  '\t' << itr->second << '\n';
    }
    cout << endl; }
    int main(){
        map<int,string>m{{1,"mithlesh"},{2,"alok"},{3,"anil"},{4,"anand"},{5,"manish"}};
        display(m);
        int x;
        string str;
        cout<<"ENTER THE MAP PAIR DATA:"<<endl;
        int n;
        cout<<"HOW MANY PAIR DATA U WANT TO ENTER:"<<endl;
        cin>>n;
        for(int i=1;i<=n;i++){
                cout<<"ENTER "<<i<<"KEY(int) DATA"<<endl;
                cin>>x;
                fflush(stdin);
                cout<<"ENTER "<<i<<"VALUE(string) DATA"<<endl;
                getline(cin,str);
                m.insert(pair<int,string>(x,str));
        }
        display(m);
        cout<<m.size();
        return 0;
    }



