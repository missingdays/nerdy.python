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

vector<string> answ;

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);

    int k;
    cin >> k;
    string s;
    cin >> s;

    vector<string> answ;
    string cur = "";
    set<char> used;

    for(int i = 0; i < s.size(); i++){
        if(used.count(s[i]) == 0){
            if(cur.size() > 0){
                answ.push_back(cur);
            }

            cur = "";
            cur += s[i];
            used.insert(s[i]);
        } else {
            cur += s[i];
        }
    }

    answ.push_back(cur);

    if(answ.size() < k){
        cout << "NO" << endl;
        return 0;
    }

    cout << "YES" << endl;
    
    int n = answ.size();
    for(int i = k; i < n; i++){
        answ[k-1] += answ[i];
    }

    for(int i = 0; i < k; i++){
        cout << answ[i] << endl;
    }
}



