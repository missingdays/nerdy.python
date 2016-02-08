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

    const int MAX = 1001;

    int n, m;
    cin >> n >> m;

    int prev[MAX], next[MAX];

    memset(prev, 0, sizeof(prev));
    memset(next, 0, sizeof(next));

    for(int i = 0; i < n; i++){
        int k;
        cin >> k;
        k %= m;

        for(int i = 0; i <= m; i++){
            if(prev[i] == 1){
                next[(i+k)%m] = 1;
            }
        }

        for(int i = 0; i <= m; i++){
            if(next[i] == 1){
                next[i] = 0;
                prev[i] = 1;
            }
        }

        prev[k] = 1;
        if(prev[0] == 1){
            puts("YES");
            return 0;
        }
    }

    puts("NO");
    return 0;
}



