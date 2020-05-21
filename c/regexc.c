
#include<stdio.h>
#include <regex.h>
int main() {
    regex_t r1,r2,r3;
    int r;
    r = regcomp(&r1,"[a*]",0);
    r = regcomp(&r2,"[a*b+]",0);
    r = regcomp(&r3,"[abb]",0);
   char in[20];
   scanf("%s",in);

   if(regexec(&r1, in, 0, NULL, 0)==0)
    printf("[a*]\n");
   if(regexec(&r2, in, 0, NULL, 0)==0)
    printf("[a*b+]\n");
   if(regexec(&r3, in, 0, NULL, 0)==0)
    printf("[abb]\n");
    return 0;
}
