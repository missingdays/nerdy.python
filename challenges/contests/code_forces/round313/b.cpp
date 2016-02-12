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
    
    int a, b, a1, b1, a2, b2;
    cin >> a >> b;
    cin >> a1 >> b1;
    cin >> a2 >> b2;

    bool ok = false;

    if(a1+a2 <= a){
        if(max(b1, b2) <= b){
            ok = true;
        }
    } 
    
    if(a1+b2 <= a){
        if(max(a2, b1) <= b){
            ok = true;
        }
    } 
    
    if(a2+b1 <= a){
        if(max(a1, b2) <= b){
            ok = true;
        }
    } 
    
    if(b1+b2 <= a){
        if(max(a1, a2) <= b){
            ok = true;
        }
    }

    if(a1+a2 <= b){
        if(max(b1, b2) <= a){
            ok = true;
        }
    } 
    
    if(a1+b2 <= b){
        if(max(a2, b1) <= a){
            ok = true;
        }
    } 

    if(a2+b1 <= b){
        if(max(a1, b2) <= a){
            ok = true;
        }
    } 
   
    if(b1+b2 <= b){
        if(max(a1, a2) <= a){
            ok = true;
        }
    }

    if(ok){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}



