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

struct cmp {
    const bool operator() (pii a, pii b){
        return a.first < b.first;
    }
};

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n;
    cin >> n;
    n++;
    vector<int> a(n);
    vector<int> count(n);

    for(int i = 0; i < n; i++){
        count[i] = 0;
    }

    for(int i = 1; i < n; i++){
        cin >> a[i];
        
        if(a[i] < n){
            count[a[i]]++;
        }
    }

    int next = 1;
    for(int i = 1; i < n; i++){
        while(next < n && count[next] != 0){
            next++;
        }

        if(next == n){
            next--;
        }

        if(a[i] >= n){
            a[i] = next;
            count[next] += 1;
        } else if(count[a[i]] > 1){
            count[a[i]] -= 1;
            a[i] = next;
            count[next] += 1;
        }
    }

    for(int i = 1; i < n; i++){
        cout << a[i] << " ";
    }

    cout << endl;
}




