#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
  int main(){
        START:
        int n;
        char states[30];
        char capital[30];
         cout<<"HOW MANY STATES AND IT'S CAPITAL U WANT U ENTER:?"<<endl;
         cin>>n;
         ofstream fout;
         fout.open("STATES",ios::app);
         cout<<"ENTER STATES AND ITS CAPITAL RESPECTFULLY"<<endl;
         for(int i=1;i<=n;i++){
            cin>>states>>capital;
            fout<<states<<" "<<capital<<endl;
         }
         fout.close();
         ifstream fin;
         char line[100];
         fin.open("STATES");
         while(!fin.eof()){
               fin.getline(line,100);
         cout<<line<<endl;
        // fin>>states>>capital;
         //cout<<states<<" "<<capital<<endl;
         }
         cout<<"DO U WANT TO APPEND SOMETHING ELSE TO THE FILE?"<<endl;
         cout<<"ENTER 0 or 1"<<endl;
         cin>>n;
         if(n)
            goto START;
         else return 0;
  }
