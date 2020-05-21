#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
int main(){
    cout<<"enter string"<<endl;
    string str;
    getline(cin,str);
    ofstream fout;
    fout.open("text.txt");
    fout.write((char*)&str,sizeof(str));
    ifstream fin;
    getch();
    fin.open("text.txt");
    fin.read((char*)&str,sizeof(str));
    cout<<str;
    return 0;
    }
