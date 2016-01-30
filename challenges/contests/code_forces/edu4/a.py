#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]

n, p, q = read_list()

s = input()

l, r = -1, -1

for i in range(n+1):
    for j in range(n+1):
        if i*p + j*q == n:
            l = i
            r = j
ns = []

if l == -1:
    print(-1)
    exit()

for i in range(0, l*p, p):
    ns.append(s[i:i+p])
for i in range(l*p, n, q):
    ns.append(s[i:i+q])

print(len(ns))
for n in ns:
    print(n)
