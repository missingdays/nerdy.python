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

const int big = 1000005;
vector<bool> vs(big);
vector<int> cur(big);

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++){
        char c;
        int v;
        cin >> c >> v;

        if(c == '-'){
            if(vs[v]){
                cur[i] = cur[i-1]-1;
                vs[v] = false;
            } else {
                for(int j = i; j > -1; j--){
                    cur[j]++;
                }
                cur[i] = cur[i-1]-1;
            }
        } else {
            cur[i] = cur[i-1]+1;
            vs[v] = true;
        }
    }
    
    int m = 0;
    for(int i = 0; i <= n; i++){
        if(cur[i] > m){
            m = cur[i];
        }
    }

    cout << m << endl;

}



