#include <stdio.h>
//Функция, находящая длину массива
//Каждая строка заканчивается на символ == 0
int len(char A[]){
    int g=0;
    while (A[g]!=0) {
        g++;
    }
    return g;
}

int main(void)
{
    //Основная строка
    char A[] = " hello world my name is Dasha. This is such a great world!";
    //Подстрока, которую будем искать
    char B[] = "world";

    //Итератор
    int i;

    //Указатель на начало подстроки сравнения
    int v=0;

    //Сколько символов подстроки совпало
    int j;

    for (i = 0; i < len(A); i++){

      j=0;
      v=i;

      while(A[v] == B[j])  {
          j++;
          v++;
      }

      if(j==len(B)) {
          //Печатаем, на какой позиции нашли подстроку
          printf("%d found \n",i);
      }

    }

    return 0;
}
