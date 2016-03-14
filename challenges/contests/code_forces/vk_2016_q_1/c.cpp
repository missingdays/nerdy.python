
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

const int big = 1005;

int ham[big][big];

int calc_ham(string& s1, string& s2){
    int ret = 0;

    for(int i = 0; i < s1.size(); i++){
        if(s1[i] != s2[i]){
            ++ret;
        }
    }

    return ret;
}

int main(int argc, const char *argv[]){ 
    
    int n, min_ham = 6;

    cin >> n;

    if(n == 1){
        cout << 6 << endl;
        return 0;
    }

    vector<string> v(n);

    for(int i = 0; i < n; i++){
        cin >> v[i];
    }

    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            min_ham = min(min_ham, calc_ham(v[i], v[j]));
        }
    }

    if(min_ham <= 2){
        cout << 0 << endl;
    } else if(min_ham <= 4){
        cout << 1 << endl;
    } else {
        cout << 2 << endl;
    }

}
