/*
 * bytelandian_gold_coins.cpp
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

int mem[100000] = {0};
unsigned long int rec(unsigned long int n){
    unsigned long int s = 0;
    if(n < 12){
        return n;
    } else if(n < 100000){
        if(mem[n]){
            return mem[n];
        }

        s = rec(n/2) + rec(n/3) + rec(n/4);
        mem[n] = max(s, n);
        return max(s, n);
    } else {
        s = rec(n/2) + rec(n/3) + rec(n/4);
        return max(s, n);
    }
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    unsigned long int n;
    while(scanf("%lu", &n) != EOF){
        printf("%lu\n", rec(n));
    }
}



