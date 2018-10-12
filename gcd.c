#include <stdio.h>
main()
{
    int m,n,temp,rem=0;
    printf("Enter two numbers: \n");
    scanf("%d%d",&m,&n);

    if(m<n){
        temp = m;
        m = n;
        n = temp;
    }
    while(n != 0){
        rem = m % n;
        m = n;
        n = rem;
    }
    printf("GCD of : %d\n", m);



}
