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

vector<int> cats;
vector< vector<int> > graph;

int n, m;

int ways(int v, int from, int cats_seen){
    if(cats[v] == 1){
        cats_seen++;
    } else {
        cats_seen = 0;
    }

    if(cats_seen > m){
        return 0;
    }

    if(graph[v].size() == 1 && graph[v][0] == from){
        return 1;
    }

    int answ = 0;
    for(int i = 0; i < graph[v].size(); i++){
        if(graph[v][i] != from){
            answ += ways(graph[v][i], v, cats_seen);
        }
    }

    return answ;
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    cin >> n >> m;

    cats = vector<int>(n);

    for(int i = 0; i < n; i++){
        cin >> cats[i];
    }

    graph = vector< vector<int> >(n);

    for(int i = 0; i < n-1; i++){
        int v1, v2;
        cin >> v1 >> v2;
        v1--;
        v2--;

        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }

    cout << ways(0, -1, 0) << endl;

}



