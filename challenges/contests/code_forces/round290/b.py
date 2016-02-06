#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())

s = input()
t = input()

k, l = 0, 0
state = 0
hd = 0

m = {}

for i in range(n):
    if s[i] != t[i]:
        hd += 1

        cs = s[i]
        ct = t[i]
        cst = cs + ct

        if cst not in m:
            m[cst] = i+1

for pair in m:
    r = pair[1] + pair[0]

    if r in m:
        print(hd-2)
        print(m[pair], m[r])
        exit()

for pair in m:
    for p in m:
        if pair == p:
            continue

        if p[0] == pair[1] or p[1] == pair[0]:
            print(hd-1)
            print(m[pair], m[p])
            exit()


print(hd)
print(-1, -1)
