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

int n;
string s;
int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    cin >> n;
    cin >> s;

    map<char, int> c;

    for(int i = 0; i < n; i++){
        c[s[i]]++;
    }

    char r = 'R', g = 'G', b = 'B';

    if(c[r] > 0 && c[g] > 0 && c[b] > 0){
        cout << "BGR" << endl;
    } else if((c[r] > 1 && c[g] > 1) || (c[r] > 1 && c[b] > 1) || (c[g] > 1 && c[b] > 1)){
        cout << "BGR" << endl;
    } else if((c[r] > 1) && (c[g] > 0 || c[b] > 0)){
        cout << "BG" << endl;
    } else if((c[g] > 1) && (c[r] > 0 || c[b] > 0)){
        cout << "BR" << endl;
    } else if((c[b] > 1) && (c[r] > 0 || c[g] > 0)){
        cout << "GR" << endl;
    } else if(c[b] > 0 && c[r] > 0){
        cout << "G" << endl;
    } else if(c[r] > 0 && c[g] > 0){
        cout << "B" << endl;
    } else if(c[b] > 0 && c[g] > 0){
        cout << "R" << endl;
    } else if(c[b] > 0){
        cout << "B" << endl;
    } else if(c[r] > 0){
        cout << "R" << endl;
    } else{
        cout << "G" << endl;
    }

    return 0;
}



