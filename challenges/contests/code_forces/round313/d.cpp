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

string smallest(string s){
    if(s.size()%2 == 1){
        return s;
    }

    string s1 = smallest(s.substr(0, s.size()/2));
    string s2 = smallest(s.substr(s.size()/2, s.size()));

    if(s2 > s1){
        return s1+s2;
    } else {
        return s2+s1;
    }

}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    string s1, s2;
    cin >> s1;
    cin >> s2;

    if(smallest(s1) == smallest(s2)){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}



