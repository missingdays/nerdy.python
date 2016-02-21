/*
 * b.cpp
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
    
    int n, answ = 0;

    cin >> n;

    vector<int> a(1 << (n+1), 0);

    for(int i = 2; i < (1<<(n+1)); i++){
        cin >> a[i];
    }

    for(int i = (1 << n)-1; i > 0; i--){
        answ += abs(a[i*2] - a[i*2+1]);
        a[i] += max(a[i*2], a[i*2+1]);
    }

    cout << answ << endl;
}



