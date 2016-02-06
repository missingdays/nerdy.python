/*
 * c.cpp
 * Copyright (C) 2016 missingdays <missingdays@missingdays>
 *
 * Distributed under terms of the MIT license.
 */

#include "bits/stdc++.h"

#define FOR(i,a,b) for(auto i=a; i!=b+1-2*(a>b); i+=1-2*(a>b))
#define REP(i,a,b) for(auto i=a-(a>b); i!=b-(a>b); i+=1-2*(a>b))
#define ALL(v) v.begin(),v.end()
#define what_is(x) cout<<#x<<" is "<<x<<endl;
#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)
#define SIZE 1000005
#define MAXN 1000000007
#define PI 3.141592653589793

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int W, H, N, num;

char ch;

multiset<int> maxHor, maxVert;
set<int> hor, vert;
LL maxArea;

LL findMax(char cut){
    auto med = ( (cut == 'H') ? (hor.find(num)) : (vert.find(num)) );
    auto big = med;
    auto sml = med;

    ++big;
    --sml;

    if(cut == 'H'){
        maxHor.erase(maxHor.find(*big-*sml));
        maxHor.insert(*big-*med);
        maxHor.insert(*med-*sml);
    } else {
        maxVert.erase(maxVert.find(*big-*sml));
        maxVert.insert(*big-*med);
        maxVert.insert(*med-*sml);
    }

    return (LL)(*maxHor.rbegin()) * (LL)(*maxVert.rbegin());

}

int main(){
    scanf("%d %d %d", &W, &H, &N);

    hor = {0, H};
    vert = {0, W};

    maxHor = {H};
    maxVert = {W};

    FOR(i, 1, N){
        cin >> ch >> num;

        if(ch == 'H'){
            hor.insert(num);
        } else if(ch == 'V'){
            vert.insert(num);
        }

        maxArea = findMax(ch);
        printf("%I64d\n", maxArea);
    }

    return 0;
}

