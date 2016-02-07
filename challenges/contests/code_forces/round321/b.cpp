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

struct cmp{
    inline bool operator () (const pair<int, int>& a, const pair<int, int>& b){
        return a.first < b.first;
    }
};

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n,d;

    cin >> n >> d;

    vector<pii> a(n);

    for(int i = 0; i < n; i++){
        int m, s;

        cin >> m >> s;

        a[i] = pii(m, s);
    }

    sort(a.begin(), a.end(), cmp());

    ll fs = 0;
    ll cs = 0;
    int l = 0, r = 0;

    while(r < n){
        pii er = a[r];
        pii el = a[l];
        if(er.first - el.first >= d){
            fs = max(fs, cs);
            while(l < r && (er.first - a[l].first >= d)){
                cs -= a[l].second;
                l++;
            }
        } else {
            cs += er.second;
            r++;
        }
    }

    fs = max(fs, cs);

    cout << fs << endl;

    return 0;
}



