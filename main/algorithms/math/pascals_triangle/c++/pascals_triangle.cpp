/*
    type: algorithm
    theme: math
    sub-theme: calculate
    name: Pascal's triangle
    author of code: Ivan @XioYS

*/

#include <iostream>
using namespace std;
int main()
{
    int n, count = 1;
    cout << "Type the number of lines " << endl;
    cin >> n;
    int mas[n][n];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < count; j++)
        {
            if (j == 0 || j == count-1)
            {
                mas[j][i] = 1;
                cout << mas[j][i] << "    ";

            }
            else
            {
                    mas[j][i] = mas[j-1][i-1] + mas[j][i-1];
                    cout << mas[j][i] << "    ";

            }


        }
        cout << endl;
        count ++;

    }



    return 0;

}
