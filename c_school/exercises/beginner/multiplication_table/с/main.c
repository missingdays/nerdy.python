#include <stdio.h>

int main(void)
{
    int i;
    int j;
    int sys;
    printf("vvedite 1 dlya 10x; vse ostalnoye dlya 16x\n");
    scanf("%d", &sys);
    if(sys == 1)
    {
      for(i=1;i<10;i++)
      {
        for(j=1;j<10;j++)
        {
            printf("%4d", j*i);
        }
        printf("\n");
        printf("\n");
      }
    }
    else
    {
        for(i=1;i<17;i++)
        {
          for(j=1;j<17;j++)
          {
              printf("%4x", j*i);
          }
          printf("\n");
          printf("\n");
        }
    }
    return 0;
}

