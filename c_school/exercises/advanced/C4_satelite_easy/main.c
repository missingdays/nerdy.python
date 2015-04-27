#include <stdio.h>

int main(void)
{
    int k;
    scanf("%d",&k);
    int A[k];
    int max=0;
    int i;
    int j;
    for (i=0;i<k;i++){
        scanf("%d",&A[i]);
    }
    for (i=0;i<k-3;i++){
        for (j=i+3;j<k;j++){
            if(A[i]*A[j]>max){
                max=A[i]*A[j];
            }
        }
    }
    printf("%d",max);
    return 0;
}
