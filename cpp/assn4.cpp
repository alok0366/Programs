#include<iostream>
#include<vector>
using namespace std;
void display(vector<double>&v){
    for(int i=0;i<v.size();i++){
            cout<<v[i]<<" ";
    }
}
int main(){
    vector<double>v(8);
    double x;
    cout<<"ENTER 8 ELEMENTS TO VECTOR"<<endl;
    for(int i=0;i<8;i++){
        cin>>x;
        v.push_back(x);
    }
    cout<<"ELEMENTS ENTERED ARE:"<<endl;
    display(v);
    cout<<"ENTER TWO MORE ELEMENTS THAT U WANT TO ENTER IN THE ARRAY:"<<endl;
    cin>>x;
    double y;
    cin>>y;
    v.push_back(x);
    v.push_back(y);
    cout<<"AFTER ADDING,NOW ELEMENTS IN THE ARRAY IS:"<<endl;
    display(v);
    cout<<"NOW DELETING ELEMENTS FROM 3 AND 5 POSITION OF THE ARRAY:"<<endl;
    v.erase(v.begin()+3,v.begin()+5);
    display(v);
    vector<double>::iterator itr=v.begin();
        for(int i=0;i<=v.size();i++)
            itr++;
        v.erase(itr);
        display(v);
}





