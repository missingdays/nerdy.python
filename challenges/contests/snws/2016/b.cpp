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
    
    int n, s;
    cin >> n >> s;

    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    double m = (double)a[0];
    double dist = 0;

    for(int i = 1; i < n; i++){
        double diff = (double)(a[i]-a[i-1])/2;
        if(diff > m){
            m = diff;
            dist = a[i] - diff;
        }
    }

    if((double)(s-a[n-1]) > m){
        dist = s;
    }

    printf("%f\n", dist);
}



