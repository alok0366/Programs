#include<iostream>
using namespace std;
int main(){
    int r;
    int m=1,one,two,five,ten,twenty,fifty,hundred,twohundred,fivehundred,onethousand,twothousand;
    //cout<<"Enter the total money"<<endl;
   // cin>>m;
    twothousand=m/2000;
    r=m%2000;
    onethousand=r/1000;
    r=r%1000;
    fivehundred=r/500;
    r=r%500;
    twohundred=r/200;
    r=r%200;
    hundred=r/100;
    r=r%100;
    fifty=r/50;
    r=r%50;
    twenty=r/20;
    r=r%20;
    ten=r/10;
    r=r%10;
    five=r/5;
    r=r%5;
    two=r/2;
    r=r%2;
    one=r/1;
    r=r%1;
    cout<<"THE GIVEN MONEY RS "<<m<<".00"<<" CAN BE DENOMINATED AS:\n"<<"TWO-THOUSAND:"""<<twothousand<<endl<<"ONE-THOUSAND:"""<<onethousand<<endl<<"FIVE-HUNDRED:"""<<fivehundred<<endl<<"TWO-HUNDRED:"""<<twohundred<<endl<<"HUNDRED:"""<<hundred<<endl<<"FIFTY:"""<<fifty<<endl<<"TWENTY:"""<<twenty<<endl<<"TEN:"""<<ten<<endl<<"FIVE:"""<<five<<endl<<"TWO:"""<<two<<endl<<"ONE:"""<<one;
    return 0;
    }
