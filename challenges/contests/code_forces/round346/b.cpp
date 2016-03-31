
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

struct Person {
    string name;
    int score;

    Person(string n, int a){
        name = n;
        score = a;
    }
};

bool cmp(const Person &a, const Person &b){
    return a.score > b.score;
}

int main(int argc, const char *argv[]){ 
    
    int n, m;
    cin >> n >> m;

    vector<vector<Person>> a(m);
    vector<string> answ;

    for(int i = 0; i < n; i++){
        string name;
        int reg, score;
        cin >> name >> reg >> score;

        a[reg-1].push_back(Person{name, score});
    }

    for(int i = 0; i < m; i++){
        sort(a[i].begin(), a[i].end(), cmp);
    }

    for(int i = 0; i < m; i++){
        if(a[i].size() > 2 && a[i][1].score == a[i][2].score){
            answ.push_back("?");
        } else {
            answ.push_back(a[i][0].name + " "  + a[i][1].name);
        }
    }

    for(int i = 0; i < m; i++){
        cout << answ[i] << endl;
    }

}
