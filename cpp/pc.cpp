#include<iostream>
#define N 10
using namespace std;
void consumer();
typedef struct{
    int value;
}item;
int count=0,in=0,out=0,buffer[N];
    void producer(item x){
        item next_item;
        next_item.value=x.value;
            while(1){
                if(count==N){
                    cout<<"BUFFER IS FULL.NO MORE PROCESSES CAN BE PRODUCED"<<endl;
                    return;}
                buffer[in]=next_item.value;
                in=(in+1)%N;
                count++;
                cout<<"PROCESS PRODUCED"<<endl;
                if(count==1)
                    consumer();
            }
    }

     void consumer(){
        item consumed_item;
            while(1){
                if(count==0){
                    cout<<"BUFFER IS EMPTY.NO MORE PROCESSES CAN BE CONSUMED"<<endl;
                    return;}
                consumed_item.value=buffer[out];
                out=(out+1)%N;
                count--;
                cout<<"PROCESS CONSUMED"<<endl;
                if(count==N-1)
                    producer(consumed_item);
            }
    }
    int main(){
        cout<<"ENTER ANY NO"<<endl;
        item n;
        int ch;
        cin>>n.value;
        cout<<"ENTER YOUR CHOICE"<<endl;
        while(1){
        cout<<"1.PRODUCER\n2.CONSUMER\n.3.EXIT"<<endl;
        cin>>ch;
        switch(ch){
            case 1:
                producer(n);
                break;
            case 2:
                consumer();
                break;
            case 3:
                exit(0);
                break;
        }}

    return 0;
    }




