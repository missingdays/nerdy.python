/*
 * gemstones.cpp
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
    int kolvo, all = 0, tyt = 0;
    cin >> kolvo;
    string kamni[kolvo], alp = "abcdefghijklmnopqrstuvwxyz";
        for(int i = 0; i < kolvo; i++) cin >> kamni[i];
        for(int c = 0;c < 26;c++)
        {
             for(int i = 0; i < kolvo; i++)
                {
                    for(int f = 0;f < kamni[i].size();f++)
                        if(kamni[i][f] == alp[c])
                        {
                            tyt++;
                            break;
                        }



                }
            if(tyt == kolvo)
                    all++;
            tyt = 0;
        }
        cout << all;


    return 0;
}
