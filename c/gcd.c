int hcfnaive(long long int a,long long int b){
    if(b==0){
        return a;}
    else{
        return hcfnaive(b,a%b);}
}

int main(){
while(1){
    long long int m,n,z;
    scanf("%lld %lld",&m,&n);
    if(m==0 && n==0){
        break;
    }
    else{
        z=hcfnaive(m,n);
    	printf("%lld\n",z);

    }
}
return 0;}

