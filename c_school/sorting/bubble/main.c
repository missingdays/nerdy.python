#include <stdio.h>

int main(void)
{
    int n = 10; //Размер массива

    int i,k; // Итераторы

    int buf; //Буфер

    int A[n]; //Инициализация массива

    for(i = 0; i < n; i++){
        scanf("%d", &A[i]); //Считываем массив из консоли
    }

    for(i = 0; i < n; i++){

        //Пробегаемся по всему массиву
        for(k = i; k < n-1; k++){

            //Если левый элемент больше правого
            if(A[k] > A[k+1]){

                //Меняем их местами
                buf = A[k];
                A[k] = A[k+1];
                A[k+1] = buf;

            }

        }
    }

    for(i = 0; i < n; i++){
        printf("%d\n", A[i]);
    }



    return 0;
}

