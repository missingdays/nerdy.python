#include <stdio.h>

int main(void)
{
    int i,k; //Итераторы

    int n = 10; //Размер массива

    int A[n]; //Инициализация массива

    int buf; //Буффер

    //Считывание массива из консоли
    for(i = 0; i < n; i++){
        scanf("%d", &A[i]);
    }

    /*
        Основная часть
    */

    for(i = 0; i < n; i++){
        int minimum = i;
        for(k = i; k < n; k++){

            if(A[k] < A[minimum]){
                minimum = k;
            }
        }

        buf = A[i];
        A[i] = A[minimum];
        A[minimum] = buf;
    }

    //Вывод массива
    for(i = 0; i < n; i++){
        printf("%d", A[i]);
    }


    return 0;
}


