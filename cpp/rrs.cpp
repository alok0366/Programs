#include<iostream>
using namespace std;
struct pro{
    int AT,BT,BT1;
    }p[99];
    int main(){
            int n,tbt=0;
        cout<<"how many process  u want to enter?"<<endl;
            cin>>n;
            for(int i=1;i<=n;i++){
                cout<<"enter the arrival time of "<<i <<" process"<<endl;
                cin>>p[i].AT;
                cout<<"enter the burst time of "<<i <<" process"<<endl;
                cin>>p[i].BT;
                tbt=tbt+p[i].BT;
                p[i].BT1=p[i].BT;
            }
            int mina=99;
            for(int i=1;i<=n;i++){
                for(int j=1;j<=n;j++){
                    int temp,temp1;
                    if(p[j].AT<mina){
                        temp=p[j].AT;temp1=p[j].BT;
                        p[j].AT=mina;p[j].BT=mina;
                        p[j].AT=temp;p[j].BT=temp1;
                }}}

    for(int i=1;i<=n;i++)
        cout<<p[i].BT<<"\t |"<<p[i].BT1<<"\t | "<<rq[i]<<endl;
        return 0;
    }






