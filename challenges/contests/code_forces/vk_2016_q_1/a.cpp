
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
    
    map <int, int> a;
    int n, cb = -1;
    cin >> n;

    for(int i = 0; i < n; i++){
        int k;
        cin >> k;

        a[k]++;

        if(cb == -1){
            cb = k;
        }

        if(a[k] > a[cb]){
            cb = k;
        }
    }

    cout << cb << endl;
}
