#include<stdio.h>
#include<string.h>
int main()
{
   FILE *fp;
   char a[50];
   char f[50];
   int n,ns,i;
   printf("Enter file name:");
   scanf("%s",f);
   printf("Enter file no.");
   scanf("%d",&n);
   fp=fopen(f,"r");
   n--;
   if(fp==NULL)
    printf("file does not exist.");
   else
   {
    while(fgets(a,50,fp)!=NULL)
   {
       ns=0;
     char* st=strtok(a," ");
     while(ns<n)
     {
         st=strtok(NULL," ");
         ns++;
     }
     printf("%s",st);
     printf("\n");
   }
   fclose(fp);
   }
}
