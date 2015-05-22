#include <stdio.h>
int main(void) {
    const int N=5;
    int a[N];
    int i, x, s;
    for(i=0; i<N; i++)
        scanf("%d", &a[i]);
    x=0;
    s=0;
    for (i=0;i<N;i++){
        if (a[i]<999&&a[i]>100){
          x++;
          s+=a[i];
        }
    }
    if (x==0){
        printf("There is no such number");
    }
    else{
    printf("%d", s/x);
    }
}

