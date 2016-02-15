/*
 * d.cpp
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

    vector<string> a(n);
    vector< vector<int> > b(n);

    for(int i = 0; i < n; i++){
        cin >> a[i];

        for(int j = 0; j < m; j++){
            b[i].push_back(a[i][j] == 'W' ? 1 : -1);
        }
        b[i].push_back(0);
    }

    b.push_back(vector<int>());
    for(int j = 0; j <= m; j++){
        b[n].push_back(0);
    }

    int answ = 0;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(b[i][j] != b[i+1][j] + b[i][j+1] - b[i+1][j+1]){
                answ++;
            }
        }
    }

    cout << answ << endl;

}



