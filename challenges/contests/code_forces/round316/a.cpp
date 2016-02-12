/*
 * a.cpp
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

    vector< vector<int> > candidates (m);

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            candidates[i].push_back(0);
            cin >> candidates[i][j];
        }
    }

    vector<int> fm (n);

    for(int i = 0; i < m; i++){
        int cm = 0;
        for(int j = 0; j < n; j++){
            if(candidates[i][j] > candidates[i][cm]){
                cm = j;
            }
        }
        fm[cm]++;
    }

    int cm = 0;

    for(int i = 0; i < n; i++){
        if(fm[i] > fm[cm]){
            cm = i;
        }
    }

    cout << cm+1 << endl;
}



