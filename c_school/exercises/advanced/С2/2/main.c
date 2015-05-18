#include <stdio.h>

int main(void)
{
    int i,s=0,j,c=0,n;
    int A[10][10];
    for (i=0;i<10;i++){

        for (j=0;j<10;j++){
            if (A[i][j]>c){
                c=A[i][j];
                n=i;
            }
        }
    }
    for (i=0;i<10;i++){
        s+=A[n][i];

    }
    printf("%d %d",n,s);
    return 0;
}

