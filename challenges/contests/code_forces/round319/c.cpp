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

vector<int> get_primes(int n){
    n++;
    vector<bool> is_prime(n);
    for(int i = 2; i < n; i++){
        is_prime[i] = true;
    }

    vector<int> answ;
    int i = 2;
    while(i < n){
        if(is_prime[i]){
            answ.push_back(i);
            for(int j = i; j<n; j+=i){
                is_prime[j] = false;
            }
            while(i < n && !is_prime[i]){
                i++;
            }
        } else {
            i++;
        }
    }
    return answ;
}

int _pow(int prime, int power){
    int answ=1;
    for(int i = 0; i < power; i++){
        answ *= prime;
    }
    return answ;
}

int main(int argc, const char *argv[]){ 
    std::ios::sync_with_stdio(false);
    
    int n;
    cin >> n;

    vector<int> primes = get_primes(n);
    vector<int> answ;

    int s = primes.size();

    for(int i = 0; i < s; i++){
        int prime = primes[i];
        int power = 1;
        while(_pow(prime, power) <= n){
            answ.push_back(_pow(prime, power));
            power++;
        }
    }

    s = answ.size();
    cout << s << endl;
    for(int i = 0; i < s; i++){
        cout << answ[i] << " ";
    }
    cout << endl;

}



