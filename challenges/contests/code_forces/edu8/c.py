#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

from string import ascii_lowercase

def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]
def new_matrix(n, m=0):
    return [[0 for i in range(m)] for i in range(n)]

def index(s):
    return ascii_lowercase.index(s)

def add(s, k):
    return ascii_lowercase[ascii_lowercase.index(s)+k]
def sub(s, k):
    return ascii_lowercase[ascii_lowercase.index(s)-k]

n, k = read_list()
s = input()

answ = ""
for i in range(n):
    if k <= 0:
        answ += s[i]
        continue

    j = index(s[i])

    if j <= 12:
        if k > 25 - j:
            answ += "z"
            k -= (25-j)
        else:
            answ += add(s[i], k)
            k = 0
    else:
        if k > j:
            answ += "a"
            k -= j
        else:
            answ += sub(s[i], k)
            k = 0

if k > 0:
    print(-1)
else:
    print(answ)
