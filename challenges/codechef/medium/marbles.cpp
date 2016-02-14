/*
 * marbles.cpp
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

ll c(int n, int k){
    if(n == k){
        return 1;
    }

    if(n == 0 || k == 0){
        return 1;
    }

    if(k == 1 || k == n-1){
        return n;
    }

    ll d = 1;
    int i = 1;

    if(k > n/2){
        k = n - k;
    }

    ll x = n, y = 1;

    while(i <= k){
        d *= x;
        d /= y;

        x--;
        y++;

        i++;
    }

    return d;
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int m;
    cin >> m;
    while(m--){
        int k, n;
        cin >> n >> k;

        cout << c(n-1, k-1) << endl;
    }
}



