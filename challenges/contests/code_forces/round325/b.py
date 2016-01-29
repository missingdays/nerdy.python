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

b = []

b.append([int(i) for i in input().split()])
b.append([int(i) for i in input().split()])

a = [int(i) for i in input().split()]

b1s = [0]
b2s = [0]

for i in range(n-1):
    b1s.append(b[0][i])
    b1s[i+1] += b1s[i]

    b2s.insert(0, b[1][n-i-2])
    b2s[0] += b2s[1]

m = 10e9

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        c = a[i] + a[j] + b1s[i] + b1s[j] + b2s[i] + b2s[j]

        m = min(m, c)

print(m)
