#include <stdio.h>

int main(void)
{

    int a;
    scanf("%d",&a);
    int i;
    int height=1;
    for (i=0;i<a;i++){
      if (i%2==0)
         {
          height*=2;
      }
     else {
          height+=1;
      }
    }
    printf("%d",height);

    return 0;
}

