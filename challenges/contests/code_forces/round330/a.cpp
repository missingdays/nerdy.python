/*
 * a.cpp
 * Copyright (C) 2016 missingdays <missingdays@missingdays>
 *
 * Distributed under terms of the MIT license.
 */

#include <bits/stdc++.h>

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

int main(){
    int n, m;
    int a, b;
    int answ = 0;

    cin >> n >> m;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a >> b;

            if(a + b > 0){
                answ++;
            }
        }
    }

    cout << answ << endl;
}
