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

bool isDivisibleBy4(string s){
    int i = stoi(s);

    if(i%4 == 0){
        return true;
    } else {
        return false;
    }
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    string a;
    cin >> a;

    ll answ = 0;

    for(int i = 0; i < a.size(); i++){

        if(i > 0 && isDivisibleBy4(a.substr(i-1, 2))){

            answ += i;
        } 
        
        if(a[i] == '4' || a[i] == '0' || a[i] == '8'){
            answ++;
        }
    }

    cout << answ << endl;
}



