#include<iostream>
using namespace std;
int main(){
    int arr[999];
    int n,sum=0,avg=0,ct=0;
    while(1){
    cout<<"SELECT CHOICE!!!!!!"<<endl;
    cout<<"1.ENTER DATA\n2.PRINT ODD ELEMENTS\n3.PRINT EVEN ELEMENTS\n4.SUM AND AVG OF NOS\n5.MAX AND MIN\n6.PRINT IN REVERSE ORDER\n7.QUIT\n8.REMOVE DUPLICATES\n"<<endl;;
    cin>>n;
    switch(n){
        case 1:cout<<"HOW MANY DATA DO U WANT TO ENTER ?"<<endl;
                int k;
                cin>>k;
                for(int i=ct;i<k;i++){
                    cin>>arr[i];
                }
                ct=ct+k;
                cout<<endl;
                break;
        case 2: cout<<"ODD ELEMENTS ARE"<<endl;
                for(int i=0;i<ct;i++){
                    if(arr[i]%2!=0){
                        cout<<arr[i]<<" ";
                    }
                }
                cout<<endl;
                break;
        case 3:cout<<"EVEN ELEMENTS ARE"<<endl;
                for(int i=0;i<ct;i++){
                    if(arr[i]%2==0){
                        cout<<arr[i]<<" ";
                    }
                }
                cout<<endl;
                break;
        case 4:sum=0;avg=0;
                for(int i=0;i<ct;i++){
                    sum=sum+arr[i];
                }
                cout<<"SUM="<<sum<<" AVG="<<sum/ct<<endl;
                break;
        case 5: {int max1=0;
                for(int u=0;u<ct;u++){
                    if(arr[u]>max1){
                        max1=arr[u];
                    }
                }cout<<"MAX: "<<max1<<endl;
                int min1=999;
                for(int u=0;u<ct;u++){
                    if(arr[u]<min1){
                        min1=arr[u];
                    }
                }cout<<"MIN: "<<min1;
                break;}
        case 6:{for(int k=ct-1;k>=0;k--){
                cout<<arr[k]<<" ";
                }
                cout<<endl;
                break;}
        case 7:exit(0);
        case 8:{int arr2[ct];int arr12[999];int i=0;
                for(int u=0;u<ct;u++){
                    if(arr12[arr[u]]==1){
                            continue;
                    }else{
                        arr12[arr[u]]=1;
                        arr2[i]=arr[u];i++;
                    }

                }
                for(int yk=0;yk<i;yk++)
                cout<<arr2[yk]<<" ";
                break;}
    }}
    return 0;
}

