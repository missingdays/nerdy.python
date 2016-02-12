/*
 * c.cpp
 * Copyright (C) 2016 missingdays <missingdays@missingdays>
 *
 * Distributed under terms of the MIT license.
 */

#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#define ALL(v) v.begin(),v.end()
#define what_is(x) cout<<#x<<" is "<<x<<endl;
#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)
#define SIZE 1000005
#define MAXN 1000000007
#define PI 3.141592653589793

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;

    int cl = 0;

    for(int i = 1; i < n; i++){
        if(s[i] == '.' and s[i-1] == '.'){
            cl++;
        }
    }

    for(int i = 0; i < m; i++){
        int x;
        char c;
        cin >> x >> c;
        x--;

        if(c == '.'){
            if(s[x] == '.'){
                cout << cl << endl;
                continue;
            }

            s[x] = '.';

            if(x>0 && s[x-1] == '.'){
                cl++;
            }
            if(x<n-1 && s[x+1] == '.'){
                cl++;
            }
        } else {
            if(s[x] != '.'){
                cout << cl << endl;
                continue;
            }

            s[x] = c;

            if(x>0 && s[x-1] == '.'){
                cl--;
            }
            if(x<n-1 && s[x+1] == '.'){
                cl--;
            }
        }
 
        cout << cl << endl;
    }
}



