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
    //Number of rows
    int n;

    //Number of columns
    int count = 1;


    cout << "Type the number of rows " << endl;

    //Scan number of rows
    cin >> n;

    //Create new array
    int mas[n][n];

    //For every row
    for (int i = 0; i < n; i++)
    {
        //For every column
        for (int j = 0; j < count; j++)
        {

            //If calculating first or last element of the row
            if (j == 0 || j == count-1)
            {

                //It equals 1
                mas[j][i] = 1;

                //Print it
                cout << mas[j][i] << "    ";

            }
            else
            {
                //Calculate new element as sum of two elements above
                mas[j][i] = mas[j-1][i-1] + mas[j][i-1];

                //Print it
                cout << mas[j][i] << "    ";

            }


        }

        //Print new line
        cout << endl;

        //Increase number of columns
        count ++;

    }



    return 0;

}
