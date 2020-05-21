#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
//c++ program to demonstrate file handling using various streams
int main(){
    char name[20];
        ofstream out;
        out.open("test.txt");
        cout<<"what do u want to enter in the file plzz entr the data";
        cin.get(name,100);
        out<<name;
        out.close();
        getch();
        ifstream in;
        char line[30];
        in>>name;
        cout<<name;
        while(in){
            in.get(line,20);
            cout<<line;
        }
        in.close();
        return 0;
        }
