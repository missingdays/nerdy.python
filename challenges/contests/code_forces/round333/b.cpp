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
    
    int n;
    cin >> n;

    if(n == 2){
        cout << 2 << endl;
        return 0;
    }

    vector<int> a(n);

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    int ml = 0;

    int i = -1, j = 1;
    int current_max = max(a[0], a[1]);
    int current_min = min(a[0], a[1]);

    if(current_max == current_min){
        int k = 0;

        while(k < n && current_max == current_min){
            current_max = max(current_max, a[k]);
            current_min = min(current_min, a[k]);
            k++;
        }
    }

    while(j < n){
        if(a[j] > current_max){
            ml = max(ml, j-i-1);
            i = j-1;
            current_max++;
            current_min++;
            while(a[i] >= current_min && a[i] <= current_max){
                i--;
            }
        } else if(a[j] < current_min){
            ml=max(ml, j-i-1);
            i = j-1;
            current_max--;
            current_min--;
            while(a[i] <= current_max && a[i] >= current_min){
                i--;
            }
        } else {
            j++;
        }
    }

    ml = max(ml, j-i-1);

    cout << ml << endl;
}



