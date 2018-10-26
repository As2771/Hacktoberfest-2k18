//to calculate factorial of a number
#include<stdio.h>
#include<conio.h>
void main()
{   
    int i,n,x=1;
    printf("enter the value for calculating factorial = \n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {    
       x=x*i;
        if(n==i)
        {
          printf("%d=",i);
        }
        else
        {    
        printf("%d*",i);
    }    
       getch(); 
}
