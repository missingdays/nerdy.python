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
#define mod 1000000007
#define PI 3.141592653589793

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n, k;

    cin >> n >> k;

    ll answ = 1;
    ll a, b;
    
    ll max_number = 9;
    ll ten = 1;

    for(int i = 0; i+1 < k; i++){
        max_number = max_number * 10 + 9;
        ten *= 10;
    }

    int blocks = n/k;

    vector<int> aa(blocks);
    vector<int> bb(blocks);

    for(int i = 0; i < blocks; i++){
        cin >> aa[i];
    }
    for(int i = 0; i < blocks; i++){
        cin >> bb[i];
    }

    for(int i = 0; i < blocks; i++){
        vector<ll> kol(10, 0);

        a = aa[i];
        b = bb[i];
        ll sum = 0;

        for(int j = 0; j < 10; j++){
            kol[j] = (ten*(j+1)-1)/a + 1;
            if(j != b){
                sum += kol[j] - (j > 0 ? kol[j-1] : 0);
            }
        }

        answ *= sum;
        answ %= mod;
    }

    cout << answ << endl;

    return 0;
}



