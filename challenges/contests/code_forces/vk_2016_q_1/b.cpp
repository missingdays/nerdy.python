
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
typedef pair<string, int> psi;

bool cmp(const psi& a, const psi& b){
    return a.second > b.second;
}

int main(int argc, const char *argv[]){ 
    
    map<string, int> a;
    vector<psi> v;
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        string s;
        cin >> s;

        a[s] = i;
    }

    for(auto iter : a){
        v.push_back(psi(iter.first, iter.second) );
    }

    sort(v.begin(), v.end(), cmp);

    for(int i = 0; i < v.size(); i++){
        cout << v[i].first << endl;
    }

    return 0;
}
