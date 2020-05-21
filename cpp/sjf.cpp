#include<iostream>
#include<stdio.h>
using namespace std;
struct pr{
    int AT,BT;
    };
    int main(){
        struct pr p[99];
        int CT[99],TAT[99],WT[99];
        cout<<"HOW MANY PROCESS U WANT TO ENTER"<<endl;
        int n;
        cin>>n;
        for(int i=1;i<=n;i++){
            cout<<"ENTER THE ARRIVAL TIME OF THE " <<i<< " PROCESS"<<endl;
            cin>>p[i].AT;
            cout<<"ENTER THE BURST TIME OF THE " <<i << " PROCESS"<<endl;
            cin>>p[i].BT;
            }



        for(int i=1;i<=n;i++){
                cout<<p[i].CT<<endl;
           // p[i].TAT=p[i].CT-p[i].AT;p[i].WT=p[i].TAT-p[i].BT;

        }
        float atat=0,awt=0;
        for(int i=1;i<=n;i++){
            atat=atat+p[i].TAT;
        awt=awt+p[i].WT;}
        atat=atat/n;awt=awt/n;
        cout<<"AVG TAT = " <<atat<<" AVG WT = " << awt <<endl;
        return 0;
    }






