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
    
    int n;
    cin >> n;

    ll a = 0;
    ll c = 0;

    for(ll i = 1; i < 1000001; i++){
        if(a == n) break;

        if(a > n){
            cout << 0 << endl;
            return 0;
        }

        if(i % 5 == 0){
            ll j = i;
            if(j % 5 == 0){
                c++;
            }

            while(j != 0 && j % 5 == 0){
                j = j / 5;
                a++;
            }
        }

    }

    cout << 5 << endl;
    for(int i = 0; i < 5; i++){
        cout << (c*5)+i << " ";
    }
    cout << endl;
    
}


