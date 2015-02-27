#include <stdio.h>

int main(void)
{
    int i,k; //Итераторы

    int n = 10; //Размер массива

    int A[n]; //Инициализация массива

    //Считывание массива из консоли
    for(i = 0; i < n; i++){
        scanf("%d", &A[i]);
    }

    /*
        Основная часть
    */

    for(i = 0; i < n; i++){
        printf("%d", A[i]);
    }


    return 0;
}

