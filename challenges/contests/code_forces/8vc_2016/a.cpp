/*
 * a.cpp
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

string s;
int n;

int count(string sub, char c){
    int ret = 0;
    for(int i = 0; i < sub.size(); i++){
        if(sub[i] == c){
            ret++;
        }
    }

    return ret;
}

bool isOk(string sub){
    if(count(sub, 'U') == count(sub, 'D')){
        if(count(sub, 'R') == count(sub, 'L')){
            return true;
        }
    }

    return false;
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    cin >> n;
    cin >> s;

    int v;

    for(int i = 0; i < n; i++){
        for(int j = 1; j < n-i+1; j++){
            if(isOk(s.substr(i, j))){
                v++;
            }
        }
    }

    cout << v << endl;
}




