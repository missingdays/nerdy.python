
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
    
    ll a, b, s;
    cin >> a >> b >> s;

    if(a < 0){
        a = -a;
    }
    if(b < 0){
        b = -b;
    }

    if(a+b <= s && (a+b-s)%2 == 0){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
