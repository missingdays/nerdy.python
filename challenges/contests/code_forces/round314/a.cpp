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
    
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    vector<pii> answ(n);

    answ[0].first = a[1] - a[0];
    answ[0].second = a[n-1] - a[0];

    answ[n-1].first = a[n-1] - a[n-2];
    answ[n-1].second = a[n-1] - a[0];

    for(int i = 1; i < n-1; i++){
        answ[i].first = min(a[i]-a[i-1], a[i+1]-a[i]);
        answ[i].second = max(a[i]-a[0], a[n-1]-a[i]);
    }

    for(int i = 0; i < n; i++){
        cout << answ[i].first << " " << answ[i].second << endl;
    }
}



