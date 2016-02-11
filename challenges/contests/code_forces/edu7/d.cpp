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

    vector<int> a;
    for(int i = n%2 == 0 ? 1 : 2; i < n; i+=2){
        a.push_back(i);
    }
    for(int i = n-1; i>0; i-=2){
        a.push_back(i);
    }

    a.push_back(n);
    for(int i = n%2 == 0 ? 2 : 1; i < n; i+=2){
        a.push_back(i);
    }
    a.push_back(n);

    for(int i = n-2; i>0; i-=2){
        a.push_back(i);
    }

    for(int i = 0; i < n*2; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}



