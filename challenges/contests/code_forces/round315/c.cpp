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

const int maxn = 1e6+2e5+5;

int primes[maxn];
int is_not_prime[maxn];
int palindromes[maxn];

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);

    memset(palindromes, 0, sizeof(palindromes));
    memset(primes, 0, sizeof(primes));
    memset(is_not_prime, 0, sizeof(is_not_prime));
    
    int p, q;
    cin >> p >> q;

    for(int i = 2; i < maxn; i++){
        if(is_not_prime[i] == 0){
            for(int j = i; j < maxn; j+=i){
                is_not_prime[j] = 1;
            }

            primes[i] = primes[i-1]+1;
        } else {
            primes[i] = primes[i-1];
        }
    }

    for(int i = 1; i < maxn; i++){
        int id = i;
        int j = 0;

        while(id != 0){
            j = j*10 + id%10;
            id /= 10;
        }

        if(j == i){
            palindromes[i] = palindromes[i-1]+1;
        } else {
            palindromes[i] = palindromes[i-1];
        }
    }

    for(int i = maxn-5; i>0; i--){
        if(q*primes[i] <= p*palindromes[i]){
            cout << i << endl;
            return 0;
        }
    }
}



