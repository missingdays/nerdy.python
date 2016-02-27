/*
 * c.cpp
 * Copyright (C) 2016 missingdays <missingdays@missingdays>
 *
 * Distributed under terms of the MIT license.
 */
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#define ALL(v) v.begin(),v.end()
#define what_is(x) cout<<#x<<" is "<<x<<endl;
#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)
#define SIZE 1000005
#define MAXN 1000000007
#define PI 3.141592653589793

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int MEMSIZE = 1110000;
const int big = 10010;
const int MAXM = 100010;

char* ptr;
char mem[MEMSIZE];
char* word[MAXM];
char s[big];
int n, m;

int dp[big];

struct Node;

typedef Node* pNode;

struct Node {
    pNode next[26];
    int num;

    Node(){
        memset(next, 0, sizeof(next));
        num = -1;
    }
};

pNode root = new Node();

void addWord(char* w, int num){
    pNode cur = root;

    for(int i = 0; w[i]; i++){
        int let = tolower(w[i]) - 'a';

        if(cur->next[let] == NULL){
            cur->next[let] = new Node();
        }

        cur = cur->next[let];
    }

    cur->num = num;
}

int main(int argc, const char *argv[]){

    scanf("%d\n", &n);

    gets(s+1);

    scanf("%d\n", &m);

    ptr = mem;

    for(int i = 0; i < m; i++){
        gets(ptr);
        int offset = strlen(ptr)+1;

        word[i] = ptr;

        ptr += offset;

        addWord(word[i], i);
    }

    memset(dp, 255, sizeof(dp));

    dp[0] = 1e9;

    for(int i = 1; i <= n; i++){
        pNode cur = root;

        for(int j = i; j >= 0; j--){
            if(cur->num != -1 && dp[j] != -1){
                dp[i] = cur->num;
                break;
            }

            if(cur->next[s[j]-'a'] == NULL){
                break;
            }

            cur = cur->next[s[j]-'a'];
        }
    }

    vector<char*> answ;

    for(int pos = n; pos > 0; pos -= strlen(word[dp[pos]])){
        answ.push_back(word[dp[pos]]);
    }

    reverse(answ.begin(), answ.end());

    for(auto ptr: answ){
        printf("%s ", ptr);
    }

    printf("\n");
    return 0;
}



