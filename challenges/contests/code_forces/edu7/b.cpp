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
    
    int h, m, a, ha;
    char c;
    cin >> h >> c >> m;
    cin >> a;

    if(a > 60){
        ha = a/60;
        a %= 60;
    }

    m+=a;

    if(m > 59){
        h++;
    }

    h+=ha;
    h %= 24;
    m %= 60;

    if(h < 10){
        cout << "0" << h;
    } else {
        cout << h;
    }

    cout << ":";

    if(m < 10){
        cout << "0" << m;
    } else {
        cout << m;
    }

    cout << endl;
}



