#include<stdio.h>
int main(){
    int a[4],max;
    printf("ENTER 4 NO:\n");
    for(int i=0;i<4;i++)
    scanf("%d",&a[i]);
    max=a[0];
    if(a[1]>max)
        max=a[1];
    else if(a[2]>max)
        max=a[2];
    else if(a[3]>max)
        max=a[3];
    printf("MAXIMUM : %d",max);
    return 0;
}
