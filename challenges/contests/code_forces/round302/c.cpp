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

const int N = 505;

int a[N];
int dp[2][N][N];

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n, lines, bugs, mod;

    scanf("%d %d %d %d", &n, &lines, &bugs, &mod);

    for(int i = 0; i < n; i++){
        scanf("%d", a+i);
    }

    dp[0][0][0] = 1;

    for(int _i = 1; _i <= n; _i++){
        int i = _i%2;

        for(int j = 0; j <= lines; j++){
            for(int k = 0; k <= bugs; k++){
                dp[i][j][k] = dp[i == 0 ? 1 : 0][j][k];

                if(j > 0 && k >= a[_i-1]){
                    dp[i][j][k] += dp[i][j-1][k - a[_i-1]];
                }

                while(dp[i][j][k] >= mod) dp[i][j][k] -= mod;
            }
        }
    }

    int answ = 0;

    for(int i = 0; i <= bugs; i++){
        answ += dp[n%2][lines][i];
        while(answ >= mod) answ -= mod;
    }

    printf("%d\n", answ);

}



