#include<stdio.h>
long int bin(long int);
int main()
{
	long int n;
	printf("Enter The Decimal Number :  ");
	scanf("%ld",&n);			//TAKING NUMBER AS INPUT:
	long int binary=bin(n);
	printf("The Binary Equivalent is %ld",binary);
}


//FUNCTION BIN
long int bin(long int x)
{
	if(x==0)
		return(0);
	else
		return(x%2+10*bin(x/2));	
}
