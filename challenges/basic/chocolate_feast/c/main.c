/*
    type: challenge solution
    theme: basic
    sub-theme: basic
    name: chocolate feast
    author of code: Darya @dar-drozdova Drozdova

*/


#include <stdio.h>

int main(void)
{

    int money;
    int price;
    int change;
    int sweets=0;
    int fantiki=0;
    int g;
    scanf("%d %d %d", &money,&price,&change);
    sweets=money/price;
    fantiki=sweets;
    while (fantiki>=change) {
        g=fantiki/change;
        sweets+=g;
        fantiki-=(g*change);
        fantiki+=g;

    }
    printf("%d",sweets);

    return 0;
}
