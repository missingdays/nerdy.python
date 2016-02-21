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


int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    ll c, Hr, Hb, Wr, Wb;

    cin >> c >> Hr >> Hb >> Wr >> Wb;

    if(Wb > Wr){
        swap(Wb, Wr);
        swap(Hb, Hr);
    }

    ll answ = 0;

    if(Wr > 1000){
        for(ll r = 0; r*Wr <= c; r++){
            ll b = (c - r*Wr) / Wb;

            ll cur = r*Hr + b*Hb;

            answ = max(answ, cur);
        }
    } else {
        ll big = max(Wb*Hr, Wr*Hb);
        for(ll r = 0; r < Wb; r++){
            for(ll b = 0; b < Wr; b++){
                ll weight = r*Wr + b*Wb;

                if(weight > c){
                    continue;
                }

                ll other = (c - weight) / (Wr*Wb);
                ll cur = r*Hr + b*Hb + other*big;

                answ = max(answ, cur);
            }
        }
    }

    cout << answ << endl;
}



