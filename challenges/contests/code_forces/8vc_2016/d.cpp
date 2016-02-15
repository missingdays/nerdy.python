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

const int N = 5005;
int a[2005];

double diff[N*2];
double diff_sum[N*2];

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);

    for(int i = 0; i < N*2; i++){
        diff[i] = 0.0;
        diff_sum[i] = 0.0;
    }
    
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a, a+n);

    double prob = 1.0 / (n*(n-1)/2);

    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            diff[a[j] - a[i]] += prob;
        }
    }

    for(int i = 1; i < N; i++){
        for(int j = 1; j < N; j++){
            diff_sum[i+j] += diff[i]*diff[j];
        }
    }

    double answ = 0.0;
    double total = 0.0;

    for(int i = 1; i < N; i++){
        answ += diff[i]*total;
        total += diff_sum[i];
    }

    printf("%.17f\n", answ);
}




