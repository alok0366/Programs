#include<stdio.h>
char* reverse(char *s){
    int l,i;
    for(l=0;*(s+l)!='\0';l++);
    for(i=0;i<l/2;i++){
        char t;
        t=*(s+i);
        *(s+i)=*(s+l-i-1);
        *(s+l-i-1)=t;

    }
    return(s);
}
void main(){
char a[99];
printf("ENTER THE STRING WHICH U WANT TO REVERSE USING POINTER\n");
scanf("%s",&a);
printf("%s",reverse(a));

}
