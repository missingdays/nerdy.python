
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

bool cmp(char a, char b){
    return b < a;
}

int main(int argc, const char *argv[]){ 
    
    string s;
    vector<char> a;
    int n;
    cin >> n;
    cin >> s;

    for(int i = 0; i < n; i++){
        if(s[i] == '2' || s[i] == '3' || s[i] == '5' || s[i] == '7'){
            a.push_back(s[i]);
        } else if(s[i] == '4'){
            a.push_back('3');
            a.push_back('2');
            a.push_back('2');
        } else if(s[i] == '6'){
            a.push_back('5');
            a.push_back('3');
        } else if(s[i] == '8'){
            a.push_back('7');
            a.push_back('2');
            a.push_back('2');
            a.push_back('2');
        } else if(s[i] == '9'){
            a.push_back('7');
            a.push_back('2');
            a.push_back('3');
            a.push_back('3');
        }
    }

    sort(a.begin(), a.end(), cmp);

    for(int i = 0; i < a.size(); i++){
        cout << a[i];
    }

    cout << endl;
}
