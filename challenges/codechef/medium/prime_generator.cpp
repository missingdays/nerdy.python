/*
 * prime_generator.cpp
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

bool check_prime(ll x){
    
    if(x < 2){
        return false;
    }

    if(x == 2){
        return true;
    }

    for(ll d = 2; d <= sqrt(x)+1; d++){
        if(x%d == 0){
            return false;
        }
    }

    return true;

}

void print_primes(ll i, ll j){
    for(ll x = i; x <= j; x++){
        if(check_prime(x)){
            cout << x << endl;
        }
    }
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int t;
    cin >> t;
    while(t--){
        ll i, j;
        cin >> i >> j;

        print_primes(i, j);
        cout << endl;
    }
}



