#include<iostream>
#include<graphics.h>
using namespace std;
struct points{
    int x,y;}p1,p2;
int main(){
    int gd=DETECT,gm;
    int dx,dy,p0,a,b;
    cout<<"ENTER THE CORRESPONDING (X1,Y1),(X2,Y2) COORDINATES"<<endl;
    cin>>p1.x>>p1.y>>p2.x>>p2.y;
    dx=abs(p2.x-p1.x);dy=abs(p2.y-p1.y);
    p0=2*dy-dx;
    a=2*dy;
    b=2*(dy-dx);
    initgraph(&gd,&gm,NULL);
    for(int i=0;i<dx;i++){
        if(p0<0){
            putpixel(p1.x+1,p1.y,RED);
            p0=p0+a;
        }
        else{
            putpixel(p1.x+1,p1.y+1,RED);
            p0=p0+b;
        }
    }
    closegraph();
    return 0;
    }
