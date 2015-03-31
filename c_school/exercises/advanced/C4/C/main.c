#include <stdio.h>
int stringToInt(char A[]){
 int r;
 r=A[1]-'0';
 if (r>=0&&r<10){

    return (A[0]-'0')*10+r;

 }
 else {
     return A[0]-'0';
 }

}

int main(void)
{
    int A[100];
    int n,i,max;
   scanf("%d",&n);
   for(i=0; i < 100; i++){
       A[i]=0;
   }
  for(i=0;i<n;i++){
      char c;
       do{
          c=getchar();
          }
          while (c!=' ');
      do{
         c=getchar();
         }
         while (c!=' ');

    char d;
    d=getchar();
    char f=getchar();

    char B[] = {d, f};
    int e;
    e=stringToInt(B);

    A[e]++;


    }
  max=A[0];

  for (i=0;i<100;i++){
      if (A[i]>max){
          max=A[i];
      }


  }
  for (i=0;i<100;i++){
      if (A[i] == max){
        printf("%d\n", i);
      }
  }

    return 0;
}

