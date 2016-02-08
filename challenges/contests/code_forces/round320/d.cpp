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
    
    ll size = 200005;
    ll a[size]; 

    ll n, k, x;
    cin >> n >> k >> x;

    for(ll i = 1; i <= n; i++){
        cin >> a[i];
    }

    ll mul = 1;
    while(k--){
        mul *= x;
    }

    ll prefix[size];
    ll suffix[size];

    for(ll i = 1; i <= n; i++){
        prefix[i] = prefix[i-1] | a[i];
    }

    for(ll i = n; i > 0; i--){
        suffix[i] = suffix[i+1] | a[i];
    }

    ll m = 0;

    for(ll i = 1; i <= n; i++){
        m = max(m, prefix[i-1] | (a[i]*mul) | suffix[i+1]);
    }

    cout << m << endl;
}



