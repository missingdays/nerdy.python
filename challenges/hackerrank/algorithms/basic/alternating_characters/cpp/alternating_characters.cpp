/*
 * alternating_characters.cpp
 * Copyright (C) 2015 missingdays <missingdays@missingdays>
 *
 * Distributed under terms of the MIT license.
 * Code by Slava Sobakin
 */

#include <iostream>
#include <string>

using namespace std;


int main()
{
    int kolvo = 0, i, j, f, size;
    string s;
    cin >> f;
    for(j = 0;j<f;j++)
    {
        i = 0;
        cin >> s;
        size = s.size();
        while(i < size-1)
        {
            if(s[i] == s[i+1])
            {
                s.erase(i+1,1);
                kolvo++;
                size = s.size();
            }
            else
                i++;
        }
        cout << kolvo << endl;
        kolvo = 0;
    }
    return 0;
}
