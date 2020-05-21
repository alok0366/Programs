#include<stdio.h>
#include<graphics.h>
struct points{
    int x,y;
    }p1,p2;
int main(){
    int gd=DETECT,gm;
    int i,dt,ds,dx,dy,d;
    printf("ENTER THE CORRESPONDING P1 AND P2 X AND Y COORDINATES \n");
    scanf("%d%d%d%d",&p1.x,&p1.y,&p2.x,&p2.y);
    dx=p2.x-p1.x;dy=p2.y-p1.y;dt=2*(dy-dx);
    ds=2*dy;
    d=2*dy-dx;
    initgraph(&gd,&gm,NULL);
    putpixel(p1.x,p1.y);
    while(p1.x<p2.x){
        p1.x++;
        if(d<0){
            d=d+ds;
        }
        else{
            p1.y++;
            d=d+dt;
        }
        putpixel(p1.x,p2.y);

    }
}



