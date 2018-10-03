#include<stdio.h>
int main() {
    int i,n,x=1;
    printf("enter the value for calculating factorial\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {x = x*i;}
    printf("value of %d! is %d",n,x);
}
