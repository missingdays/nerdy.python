/*
 * utopian_tree.cpp
 * Copyright (C) 2015 missingdays <missingdays@missingdays>
 *
 * Distributed under terms of the MIT license.
 *
 * Code by Slava Sobakin
 */

#include <iostream>

using namespace std;


int main()
{
    int cycles, rost = 1;
    int i, j, f;
    cin >> j;
    for(f = 0;f<j;f++)
    {
        cin >> cycles;
        for(i = 0; i < cycles; i++)
        {
            if(i % 2 == 0)
            {
                rost *= 2;
            }
            else
            {
                rost += 1;
            }
        }
        cout << rost << endl;
        rost = 1;
    }
    return 0;
}
