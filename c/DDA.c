#include<stdio.h>
#include<math.h>
struct points{
    int x,y;
    }p1,p2;
int main(){
    int steps,i,dx,dy;
    float x_inc,y_inc;
    printf("ENTER THE CORRESPONDING P1 AND P2 X AND Y COORDINATES \n");
    scanf("%d%d%d%d",&p1.x,&p1.y,&p2.x,&p2.y);
    dx=p2.x-p1.x;dy=p2.y-p1.y;
    if(abs(dx)>abs(dy)){
        steps=abs(dx);
    }
    else{
        steps=abs(dy);
    }
    x_inc=(float)dx/steps;y_inc=(float)dy/steps;
    float x=p1.x,y=p1.y;
    for(i=0;i<=steps;i++){
        printf("CORRESPONDING PIXELS ARE P%d:(%.f,%.f)\n",i+1,round(x),round(y));
        x=x+x_inc;
        y=y+y_inc;
    }
}
