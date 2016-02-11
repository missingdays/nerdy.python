/*
 * c.cpp
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

vector<int> numbers (202020);
vector<int> nxt (2010101);

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n, m;

    scanf("%d %d", &n, &m);

    for(int i = 0; i < n; i++){
        int x;
        scanf("%d", &x);

        numbers[i] = x;
    }

    nxt[n] = n;
    for(int i = n-1; i >= 0; i--){
        if(numbers[i] == numbers[i+1]){
            nxt[i] = nxt[i+1];
        } else {
            nxt[i] = i+1;
        }
    }

    while(m--){
        int l, r, x;
        scanf("%d %d %d", &l, &r, &x);

        l--;
        r--;

        if(numbers[l] != x){
            cout << l+1 << endl;
        } else {
            if(nxt[l] > r){
                cout << -1 << endl;
            } else {
                cout << nxt[l] + 1 << endl;
            }
        }
    }

}



