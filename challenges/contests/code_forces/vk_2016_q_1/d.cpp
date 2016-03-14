
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

struct Platform {
    Platform *next, *prev;
    int first, second;

    Platform(int l, int r, Platform *p){
        next = NULL;
        prev = p;
        first = l;
        second = r;
    }
};

int main(int argc, const char *argv[]){ 
    
    int n, m, s, d;
    scanf("%d %d %d %d\n", &n, &m, &s, &d);
    vector<int> pr(n); // препятствия

    for(int i = 0; i < n; i++){
        scanf("%d ", &pr[i]);
    }

    sort(pr.begin(), pr.end());

    Platform *first = new Platform(0, pr[0]-1, NULL);
    Platform *cur = first;

    for(int i = 1; i < n; i++){
        cur->next = new Platform(pr[i-1]+1, pr[i]-1, cur);
        cur = cur->next;
    }
    cur->next = new Platform(pr[n-1]+1, m, cur);

    cur = first;

    while(cur->next != NULL){

        if(cur->second - cur->first < s){
            if(cur->first == 0){
                puts("IMPOSSIBLE");
                return 0;
            }

            cur->prev->next = cur->next;
            cur->next->prev = cur->prev;
        }

        cur = cur->next;
    }

    cur = first;

    while(cur->next != NULL){

        if(cur->second + d < cur->next->first){
            puts("IMPOSSIBLE");
            return 0;
        }

        cur = cur->next;
    }

    cur = first;

    while(cur->next != NULL){
        printf("RUN %d\n", cur->second - cur->first);
        printf("JUMP %d\n", cur->next->first - cur->second);

        cur = cur->next;
    }

    if(cur->second - cur->first != 0)
        printf("RUN %d\n", cur->second - cur->first);

    return 0;
}
