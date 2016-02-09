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

int gcd(int a, int b){
    while(a > 0 and b > 0){
        if(a > b){
            a %= b;
        } else {
            b %= a;
        }
    }
    return max(a, b);
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n;
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    int prefix[n];
    int suffix[n];
    
    prefix[0] = a[0];
    suffix[n-1] = a[n-1];

    for(int i = 1; i < n; i++){
        prefix[i] = gcd(a[i], prefix[i-1]);
    }
    for(int i = n-2; i > -1; i--){
        suffix[i] = gcd(a[i], suffix[i+1]);
    }

    int j = 0;
    int m = 0;

    if(suffix[1] >= prefix[n-2]){
        m = suffix[1];
        j = 1;
    } else {
        m = prefix[n-2];
        j = n;
    }

    for(int i = 1; i < n-1; i++){
        int g = gcd(prefix[i-1], suffix[i+1]);
        if(g > m){
            m = g;
            j = i+1;
        }
    }

    cout << j << " " << m << endl;
}



