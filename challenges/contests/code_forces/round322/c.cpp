/*
 * c.cpp
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


struct cmp {
    inline bool operator() (const int& a, const int& b){
        return (10-(a%10)) < (10-(b%10));
    }
};

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n, k;

    cin >> n >> k;

    vector<int> a(n);

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end(), cmp());

    for(int i = 0; i < n; i++){
        if(k <= 0){
            break;
        }
        
        int left = 10 - (a[i]%10);

        if(left <= k){
            if(a[i] + left <= 100){
                a[i] += left;
                k -= left;
            } else {
                k -= 100-a[i];
                a[i] = 100;
            }
        }
    }

    int answ = 0;

    for(int i = 0; i < n; i++){
        answ += a[i]/10;

        if(k >= 10 && a[i] < 100){
            int left = 100-a[i];

            if(left <= k){
                answ += left/10;
                k -= left;
            } else {
                answ += k/10;
                k = 0;
            }
        }
    }

    cout << answ << endl;
}



