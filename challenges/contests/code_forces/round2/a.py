#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

n = int(input())
r = []
p = {}

for i in range(n):
    a, b = input().split()
    score = int(b)
    if a in p:
        p[a] += score
    else:
        p[a] = score
    r.append([a, p[a]])

m = 0
winners = []

for key in p:
    if p[key] > m:
        m = p[key]

for key in p:
    if p[key] == m:
        winners.append(key)

for i in range(n):
    if r[i][1] >= m and r[i][0] in winners:
        print(r[i][0])
        exit()
