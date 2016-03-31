
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#define what_is(x) cout<<#x<<" is "<<x<<endl;
#define MAXN 1000000007
#define PI 3.141592653589793

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

vector<vector<int>> graph;
vector<bool> visited;

int visit(int i, int from){
    if(visited[i]){
        return 1;
    }

    visited[i] = true;

    for(int j = 0; j < graph[i].size(); j++){
        if(graph[i][j] == from){
            continue;
        }
        int k = visit(graph[i][j], i);

        if(k == 1){
            return 1;
        }
    }

    return 0;
}

int main(int argc, const char *argv[]){ 
    
    int n, m;
    cin >> n >> m;

    graph = vector<vector<int>>(n);
    visited = vector<bool>(n);

    for(int i = 0; i < n; i++){
        visited[i] = false;
    }

    for(int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        a--;
        b--;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int answ = 0;
    for(int i = 0; i < n; i++){
        if(!visited[i]){
            answ += 1-visit(i, -1);
        }
    }

    cout << answ << endl;
}
