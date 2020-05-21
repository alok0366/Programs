#include<stdio.h>
#include<stdlib.h>
int main(){
    int a[50];int x,i,m,y;
    printf("\t!!!this is c program to find any no using binary search and return its index no!!!\n");
    printf("how many no u want to enter\n");
    scanf("%d",&x);
    for(i=0;i<x;i++)
        scanf("%d",&a[i]);
        printf("enter the no which u want search\n");
        scanf("%d",&y);
    binary_search(a,x,y);
    return 0;
    }
    int binary_search(int a[],int x,int y){
        int u=0;int v=x-1;int m;
        while(u<=v){
            m=(u+v)/2;
            if(y==a[m]){
                printf("search successful...item found at %d",m);
                    return;
                    }
        else if(y>=a[m])
            u=m+1;
            else
                u=m-1;
        }
    }
