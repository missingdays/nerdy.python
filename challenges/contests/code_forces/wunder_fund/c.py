#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def not_line(a, b, c):
    if a[0] == b[0]:
        return a[0] != c[0]
    if a[1] == b[1]:
        return a[1] != c[1]
    if a[0] == c[0]:
        return a[0] != b[0]
    if a[1] == c[1]:
        return a[1] != b[1]
    if b[0] == c[0]:
        return a[0] != b[0]
    if b[1] == c[1]:
        return a[1] != b[1]

    k = (b[1] - a[1]) / (b[0] - a[0])
    _b = b[1] - k * b[0]

    if c[1] != c[0]*k + _b:
        return True
    return False

n = int(input())

a = []

for i in range(n):
    a.append([int(i) for i in input().split()])
    a[i].append(i)

a.sort(key=lambda k: (k[0], k[1]))

for i in range(n-2):
    if not_line(a[i], a[i+1], a[i+2]):
        print(a[i][2]+1, a[i+1][2]+1, a[i+2][2]+1)
        exit()
