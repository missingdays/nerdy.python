#include <stdio.h>
int main(void) {
    const int N=5;
    int a[N];
    int i, x, y;
    float s;
    for(i=0; i<N; i++){
        scanf("%d", &a[i]);
    }
 x=0;
 y=0;
 for(i=0;i<N;i++){
     if (a[i]%2!=0){
         y++;
         x+=a[i];

     }
 }
 s = x / y;
printf("%f",s);
}

