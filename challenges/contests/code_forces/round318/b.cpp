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

const int big = 4005;
const int inf = 1000000007;

bool graph[big][big];
int degree[big];

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);

    memset(degree, 0, sizeof(degree));

    int n, m;
    cin >> n >> m;

    for(int i = 0; i < m; i++){
        int u, v;
        cin >> v >> u;

        graph[u][v] = true;
        graph[v][u] = true;
        degree[v]++;
        degree[u]++;
    }

    int answ = inf;

    for(int i = 1; i <= n; i++){
        for(int j = i+1; j<=n; j++){
            if(graph[i][j]){
                for(int k = j+1; k<= n; k++){
                    if(graph[i][k] && graph[j][k]){
                        answ = min(answ, degree[i]+degree[j]+degree[k]);
                    }
                }
            }
        }
    }

    if(answ == inf){
        cout << -1 << endl;
    } else {
        cout << answ-6 << endl;
    }

    return 0;

}



