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

a = []

for i in range(n):
    a.append([int(i) for i in input().split()])

b = [0 for i in range(n)]
c = {}

for i in range(n):
    for j in range(n):
        c[j] = 0

    for j in range(n):
        c[a[i][j]] += 1

    for j in range(n):
        if j in c and c[j] > 1:
            b[i] = j 

i1 = -1
m = 0

for i in range(n):
    if b[i] == 0:
        l = max(a[i])

        if l > m:
            m = l
            i1 = i

b[i1] = n-1

for i in range(n):
    if b[i] == 0 and i != i1:
        b[i] = n

for e in b:
    print(e, end=" ")
print()
