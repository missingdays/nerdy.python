#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def dist(a, b):
    return pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2)

n, x1, y1, x2, y2 = [int(i) for i in input().split()]

fls = []
r1 = 0
r2 = 0

for i in range(n):
    fls.append([[int(i) for i in input().split()], True])

for i in range(n):
    fls[i][1] = dist(fls[i][0], [x1, y1]) + dist(fls[i][0], [x2, y2])

fls.sort(key=lambda e: -e[1])

for i in range(n):
    fl = fls[i][0]

    d1 = dist(fl, [x1, y1])
    d2 = dist(fl, [x2, y2])

    if d1 > r1 and d2 > r2:
        m1 = r1 + d2
        m2 = r2 + d1

        if m1 < m2:
            r2 = d2
        else:
            r1 = d1

print(r1 + r2)
