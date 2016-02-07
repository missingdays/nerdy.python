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

const int N = 1000;

map <int, int> cnt;
int answ[N];

int gcd(int a, int b){
    while(b > 0 && a > 0){
        if(b > a){
            b %= a;
        } else {
            a %= b;
        }
    }

    return max(a, b);
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n;
    scanf("%d", &n);

    int s = n*n;

    for(int i = 0; i < s; i++){
        int a;
        scanf("%d", &a);
        cnt[-a]++;
    }

    int pos = n-1;

    for(auto it = cnt.begin(); it != cnt.end(); it++){
        int x = -it->first;

        while(it->second){
            answ[pos] = x;
            --it->second;

            for(int i = pos+1; i<n; i++){
                cnt[-gcd(answ[pos], answ[i])] -= 2;
            }

            pos--;
        }
    }

    for(int i = 0; i < n; i++){
        printf("%d ", answ[i]);
    }

    return 0;

}



