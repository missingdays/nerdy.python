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
    
    int n;
    cin >> n;
    vector<int> a(n);
    vector<ll> b(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int v1 = 0, v2 = 0;
    int answ = 2;

    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){

            int f = -1;
            b[0] = a[i];
            b[1] = a[j];

            for(int i = 2; i < n; i++){
                b[i] = b[i-1] + b[i-2];
            }

            for(int k = 0; k < n; k++){
                if(a[k] == b[2]){
                    f = k;
                    break;
                }
            }

            if(f == -1)
                continue;

            int p = 2;
            for(int k = f; k < n; k++){
                if(a[k] == b[p]){
                    p++;
                }
            }

            answ = max(answ, p);
        }
    }

    cout << answ << endl;
}



