#include<iostream>
#include<map>
#include<iterator>
using namespace std;
int main(){
    map<int,int>m;
    int n;
    cout<<"ENTER THE NOs FOR WHICH U WANT TO REMOVES DUPLICATE"<<endl;
    while(cin>>n){
        m.insert(pair<int,int>(n,n));
    }
    map<int,int>::iterator itr;
    for(itr=m.begin();itr!=m.end();itr++){
        cout<<itr->second<<endl;
    }
}
