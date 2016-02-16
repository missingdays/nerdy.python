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
    
    int n, k;
    cin >> n >> k;

    vector<string> answ;

    int f = 0;
    for(int i = 0; i < n; i++){
        answ.push_back("");

        for(int j = 0; j < n; j++){
            if(j%2 == i%2 && f < k){
                answ[i] += 'L';
                f++;
            } else {
                answ[i] += 'S';
            }
        }
    }

    if(f == k){
        cout << "YES" << endl;

        for(int i = 0; i < n; i++){
            cout << answ[i] << endl;
        } 
    } else {
        cout << "NO" << endl;
    }
}



