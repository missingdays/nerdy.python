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

int n, k, a, m, ships;
set<pii> xs;

int calc(int l, int r){
    return (r-l+2)/(a+1);
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    cin >> n >> k >> a >> m;

    xs.insert(pii(n, 1));
    ships = calc(1, n);

    for(int i = 0; i < m; i++){
        int x, newk1 = 0, newk2 = 0;

        cin >> x;

        auto it = xs.lower_bound(pii(x, -1));

        int l = it->second, r = it->first;

        if(x-1 >= l){
            newk1 = calc(l, x-1);
        }
        if(x+1 <= r){
            newk2 = calc(x+1, r);
        }

        ships -= calc(l, r);
        ships += newk1+newk2;

        if(ships < k){
            cout << i+1 << endl;
            return 0;
        }

        xs.erase(it);
        if(x-1 >= l){
            xs.insert(pii(x-1, l));
        }
        if(x+1 <= r){
            xs.insert(pii(r, x+1));
        }
    }

    cout << -1 << endl;
    return 0;
}



