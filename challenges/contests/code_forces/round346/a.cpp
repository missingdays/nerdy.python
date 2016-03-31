
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
    int n, a, b;

    cin >> n >> a >> b;

    a += b;

    int r;
    if(a >= 0){
        r = a%n;
    } else {
        r = n - abs(a)%n;
    }
    cout << (r == 0 ? n : r) << endl;
}
