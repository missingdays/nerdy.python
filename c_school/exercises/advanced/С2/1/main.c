#include <stdio.h>

int main(void)
{

    int i,s=0,n=0,g=0,j;
    int A[10][20];
    for (i=0;i<10;i++){
        g=0;
        for (j=0;j<20;j++){
           g+=A[i][j];
        }
        if (g>s){
            s=g;
            n=i;
        }
    }
    printf ("%d %d",n,s);
    return 0;
}

