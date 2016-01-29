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

eps = 1e-9

x1, x2 = [int(i) for i in input().split()]

x1 += eps
x2 -= eps

area1 = []
area2 = []

for i in range(n):
     k, b = [int(i) for i in input().split()]

     y1 = x1 * k + b
     y2 = x2 * k + b

     area1.append([y1, i])
     area2.append([y2, i])

area1.sort(key=lambda a: a[0])
area2.sort(key=lambda a: a[0])

yep = False

l = len(area1)

for i in range(l):
    if area1[i][1] != area2[i][1]:
        yep = True
        break

if yep:
    print("YES")
else:
    print("NO")
