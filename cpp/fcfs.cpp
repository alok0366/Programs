#include<iostream>
#include<map>
using namespace std;
void display(map<int,int>&m){
    map<int,int>::iterator itr;
    for (itr = m.begin(); itr != m.end(); ++itr){
        cout  <<  '\t' << itr->first
              <<  '\t' << itr->second << '\n';
    }
    cout << endl; }
int main(){
    map<int,int>p;
    int CT[99],TAT[99],WT[99],n,x,y;
    float atat,awt;
    cout<<"HOW MANY PROCESS U WANT TO ENTER"<<endl;
            cin>>n;
        for(int i=1;i<=n;i++){
            cout<<"ENTER THE " <<i<<"PROCESS ARRIVAL TIME"<<endl;
            cin>>x;
            cout<<"ENTER THE " <<i<<"PROCESS BURST TIME"<<endl;
            cin>>y;
          p.insert(make_pair(x,y));
        }
        map<int,int>::iterator itr=p.begin();
        int sum=itr->first,i=1;
    for (itr = p.begin();itr != p.end();++itr){
       sum=(sum+itr->second);
       CT[i]=sum;
       TAT[i]=CT[i]-(itr->first);
       WT[i]=TAT[i]-(itr->second);
        i++;
    }
display(p);
for(int i=1;i<=n;i++){
    cout  <<  '\t' << CT[i]<<  '\t' << TAT[i] <<'\t' << WT[i] << '\n';}
                sum=0;float sum1=0,sum2=0;
                for(int i=1;i<=n;i++){
                        sum2=sum2+TAT[i];
                        sum1=sum1+WT[i];
                }
                atat=sum2/n;
                awt=sum1/n;
                cout<< "AVERAGE TAT = "<<atat<< "\nAVERAGE WT = "<<awt<<endl;
        return 0;
}
