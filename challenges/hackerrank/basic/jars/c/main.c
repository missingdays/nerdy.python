/*
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: chocolate feast
    author of code: Darya @dar-drozdova Drozdova

*/

#include <stdio.h>

int main(void)
{int jars;
 int amount;
 int a,b,c,i,sum=0;
 scanf("%d %d", &jars, &amount);
 for(i=0;i<amount;i++){
     scanf("%d %d %d",&a,&b,&c);
     sum+=(b-a+1)*c;
           }
    printf("%d",sum/jars);
    return 0;
}
