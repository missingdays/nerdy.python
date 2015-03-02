#include <stdio.h>

int len(char A[]){
    int g=0;
    while (A[g]!=0) {
        g++;
    }
    return g;
}

int main(void)
{
    char A[] = " hello world my name is Dasha";

    char B[] = "world";

    printf("%d\n", D[1]);
    int v=0;
    int i;
    int j;
    int a = len(A);
    printf("%d \n", a);
    for (i=0;i<len(A);i++){
      j=0;
      v=i;
      while(A[v]==B[j])  {
          j++;
          v++;
      }
      if(j==len(B)) {
          printf("%d found \n",i);
      }

    }

    return 0;
}

