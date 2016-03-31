
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
    scanf("%d%d", &n, &m);

    vector<int> a(n);
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }

    sort(a.begin(), a.end());

    vector<ll> answ;

    ll ci = 0, cc = 1;
    while(m >= cc){
        if(ci < n && a[ci] == cc){
            ci++;
        } else {
            m -= cc;
            answ.push_back(cc);
        }
        cc++;
    }

    printf("%d\n", answ.size());
    for(int i = 0; i < answ.size(); i++){
        printf("%ld ", answ[i]);
    }
}
