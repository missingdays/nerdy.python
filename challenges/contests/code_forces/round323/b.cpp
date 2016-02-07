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

vector<int>a; 

int search(int l, int r, int v, bool reverse){
    if(!reverse){
        for(int i = l; i < r; i++){
            if(a[i] <= v){
                return i;
            }
        }
    } else {
        for(int i = r-1; i>=l; i--){
            if(a[i] <= v){
                return i;
            }
        }
    }

    return -1;
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    int n;
    cin >> n;

    a = vector<int>(n);

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    int inf = 0;
    bool turn_right = true;
    int cp = 0;
    int answ = 0;

    for(int i = 0; i < n; i++){
        int next;
        if(turn_right){
            next = search(cp, n, inf, false);

            if(next == -1){
                next = search(0, cp+1, inf, true);
            }
        } else {
            next = search(0, cp+1, inf, true);
            if(next == -1){
                next = search(cp, n, inf, false);
            }
        }

        if(turn_right && next < cp){
            answ++;
            turn_right = false;
        } else if(!turn_right && next > cp){
            answ++;
            turn_right = true;
        }


        cp = next;
        inf++;

        a[cp] = n+1;
    }

    cout << answ << endl;
}



