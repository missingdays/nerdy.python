#include <stdio.h>

int main(void)
{
    int a;
    int b;
    int c;

    scanf("%d",&a);
    scanf("%d",&b);
    c=a;
    a=b;
    b=c;

    printf("%d ",a);
    printf("%d ",b);


    return 0;
}

