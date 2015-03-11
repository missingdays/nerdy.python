/*
    type: algorithm
    theme: arrays
    sub-theme: sorting
    name: quick sorting
    author of code: Ivan @XioYS

*/


#include <iostream>
 void QuickSortRecurs(int  ArrToSort[], int first, int last)
{
    int  CenterEl = ArrToSort[(last+first)/2]; //This is the index of the center of the array
    int i = first, x = last;
    while (i <= x)
    {
        while(ArrToSort[i] < CenterEl){i++;}
        while(ArrToSort[x] > CenterEl) {x--;}
        if (i <= x)
        {
            int  tmp = ArrToSort[i];
            ArrToSort[i] = ArrToSort[x];
            ArrToSort[x] = tmp;
            i++;
            x--;
        }
    }
        if (first < x) {QuickSortRecurs(ArrToSort, first, x);}
        if (last > i) {QuickSortRecurs(ArrToSort,i,last);}



}
int main()
{
    int Mas[9] = {5,56,12,45,123,3,23,2351,2};
    QuickSortRecurs(Mas, 0 ,9);
    for (int i = 0; i < 9; i++)
    {
        std::cout << Mas[i] << std::endl;
    }
    return 0;
}
