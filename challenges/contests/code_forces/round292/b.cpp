
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

int main(int argc, const char *argv[]){ 
    
    int n, m;
    cin >> n >> m;
    vector<bool> boys(n);
    vector<bool> girls(m);
    int a, b;

    cin >> a;
    for(int i = 0; i < a; i++){
        int j;
        cin >> j;
        boys[j] = true;
    }

    cin >> b;
    for(int i = 0; i < b; i++){
        int j;
        cin >> j;
        girls[j] = true;
    }

    bool changed = true;
    ll count = 0;

    while(changed){
        changed = false;
        for(int i = 0; i < 2*max(n, m); i++){
            if(girls[count%m] && !boys[count%n]){
                boys[count%n] = true;
                changed = true;
            } else if(boys[count%n] && !girls[count%m]){
                girls[count%m] = true;
                changed = true;
            }
            count++;
        }
    }

    for(int i = 0; i < n; i++){
        if(!boys[i]){
            cout << "No" << endl;
            return 0;
        }
    }
    for(int i = 0; i < m; i++){
        if(!girls[i]){
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;
}
