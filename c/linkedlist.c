#include<stdio.h>
#include<stdlib.h>
struct link{
    int data;
    struct link *ptr;
};
struct link *START=NULL;
struct link* createnode(){
    struct link *p;
    p=(struct link*)malloc(sizeof(struct link));
    return(p);
    }


void insertnode(){
        struct link *temp,*t;
        temp=createnode();
        printf("ENTER THE DATA\n");
        scanf("%d",&temp->data);
        temp->ptr=NULL;
    if(START==NULL){
        START=temp;
    }
    else{
        t=START;
        while(t->ptr!=NULL){
            t=t->ptr;}
            t->ptr=temp;

    }
}
void display(){
    struct link *temp;
    if(START==NULL){
        printf("LIST IS EMPTY\n");

    }
    else{
        temp=START;
        while(temp!=NULL){
            printf("%d\n",temp->data);
            temp=temp->ptr;
        }
    }


}
void main(){
    int n;
    while(1){
    printf("ENTR THE CHOICE");
    printf("\n");
    printf("1.INSERT DATA\n2.Display\n");
    scanf("%d",&n);
    switch(n){
    case 1:
        insertnode();
        break;
    case 2:
        display();
        break;

        }

}

}
