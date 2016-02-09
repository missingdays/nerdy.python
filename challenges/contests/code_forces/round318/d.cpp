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

const int big = 1e6+2;
const int inf = 1e9+7;

int towers[big];
int res[big];
int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++){
        cin >> towers[i];
    }

    int worst = 0;
    for(int i = 1; i <= n; i++){
        worst = min(worst, towers[i]-i);
        res[i] = i + worst;
    }

    worst = n+1;

    for(int i = n; i > 0; i--){
        worst = min(worst, towers[i]+i);
        res[i] = min(res[i], worst-i);
    }
    int r = 0;

    for(int i = 1; i <= n; i++){
        r = max(r, res[i]);
    }

    cout << r << endl;
}



