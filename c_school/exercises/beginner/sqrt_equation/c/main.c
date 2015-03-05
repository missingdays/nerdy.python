#include <stdio.h>
#include <math.h>

int main(void)
{
    printf("formula ax^2+bx+c=0\nVvedi a\n");
    int a;
    scanf("%d", &a);
    printf("Vvedi b\n");
    int b;
    scanf("%d", &b);
    printf("Vvedi c\n");
    int c;
    scanf("%d", &c);
    int D = b*b - 4*a*c;
    if (D > 0) {
        int x1 =(-b-sqrt(D))/2*a;
        int x2 =(-b+sqrt(D))/2*a;
        printf("x1=%d", x1);
        printf("\nx2=%d", x2);
    }
    else{
        if (D==0){
            int x = -b/2*a;
            printf("x=%d", x);
        }
        else{
          printf("NET RESHENII, MOTHERFUCKERS");
        }

    }
return 0;
}

