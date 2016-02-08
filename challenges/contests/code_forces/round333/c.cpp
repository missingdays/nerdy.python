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

const ll BIGN = (ll)1000000007*1000000007;

int n, m;

vector< vector<int> > graph1;
vector< vector<int> > graph2;

vector<ll> distances;

void fill_graph_2(){
    for(int i = 0; i < n; i++){
        int k = 0;
        for(int j = 0; j < n; j++){
            if(i == j){
                continue;
            }
            if(k >= graph1[i].size()){
                graph2[i].push_back(j);
            } else if(graph1[i][k] == j){
                k++;
            } else {
                graph2[i].push_back(j);
            }
        }
    }
}

ll distance(vector< vector<int> > graph){

    list<int> queue(n);
    for(int i = 0; i < n; i++){
        distances[i] = BIGN;
    }

    distances[0] = 0;
    queue.push_back(0);

    while(!queue.empty()){
        int current = queue.front();
        queue.pop_front();

        for(int i = 0; i < graph[current].size(); i++){
            int u = graph[current][i];
            if(distances[u] == BIGN){
                distances[u] = distances[current]+1;
                queue.push_back(u);
            }
        }
    }

    return distances[n-1];
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);

    cin >> n >> m;

    graph1 = vector< vector<int> > (n);
    graph2 = vector< vector<int> > (n);
    distances = vector<ll> (n);

    for(int i = 0; i < m; i++){
        int u, v;

        cin >> u >> v;
        u--;
        v--;

        graph1[u].push_back(v);
        graph1[v].push_back(u);
    }

    for(int i = 0; i < n; i++){
        sort(graph1[i].begin(), graph1[i].end());
    }

    fill_graph_2();

    ll distance1 = distance(graph1);
    ll distance2 = distance(graph2);

    if(distance1 == BIGN or distance2 == BIGN){
        cout << -1 << endl;
        return 0;
    }

    cout << max(distance1, distance2) << endl;
    return 0;
}



