#include <iostream>
#include<stdio.h>
using namespace std;
bool v[1000000];
int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
   long non_self = 0;
  for(long i = 1; i < 1000000; ++i) {
    if(!(v[i]))cout<<i<<'\n';
    non_self = i + (i%10) + (i/10)%10 + (i/100)%10 + (i/1000)%10 + (i/10000)%10 +(i/100000)%10;
    v[non_self] = 1;
  }
  return 0;
}
