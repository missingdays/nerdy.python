#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

#Constant
def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]
def new_matrix(n, m=0):
    return [[0 for i in range(m)] for i in range(n)]
mod=1000000007


def binPow(a, q, mod):
    a %= mod
    if q == 0:
        return 1
    return ((q%2 == 1 and a or 1) * binPow(a*a, q//2, mod)) % mod

n = int(input())

a = {}

b = read_list()

for c in b:
    if c in a:
        a[c] += 1
    else:
        a[c] = 1

d, answ = 1, 1

for p in a:
    c = a[p]

    fp = binPow(p, (c + 1)*c//2, mod)
    answ = binPow(answ, (c+1), mod) * binPow(fp, d, mod) % mod
    d = d * (c+1) % (mod-1) 

print(answ)
