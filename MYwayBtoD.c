
#include<stdio.h>

void binary(int n)

{

    int rem;

    if(n<=1)

    {

        printf("%d",n);

        return;

    }

    rem=n%2;

    binary(n/2);

    printf("%d",rem);

}

int main()

{

    int n,c,d=0,b=1,r;

    printf("1. For decimal to binary\n");

    printf("2. for binary to decimal\n");

    scanf("%d",&c);

    printf("enter number to convert\n");

    scanf("%d",&n);

    if(c==1)

    {

        if(n<0)

        {

            printf("not possible\n");

        }

        else

        {

            printf("The decimal -> binary is ");

            binary(n);

        }

    }

    else if(c==2)

    {

        while(n>0)

        {

            r=n%10;

            d=d+(b*r);

            n=n/10;

            b=b*2;

        }

        printf("The binary -> decimal is %d\n",d);

    }

}
