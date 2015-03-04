#include <stdio.h>
    int sum (int a,int b){
        int c = 0;
        c = a+b;
        return c;
    }

    int main(void)
    {
    int a ;
    int b ;
    int d ;
    a=0;
    b=0;
    scanf("%d",&a);
    scanf("%d",&b);
    d=0;
    d = sum(a,b);
    printf("%d",d);



    return 0;
}

