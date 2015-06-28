#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())
c = []

def find_min(a):
    mini = 0
    minv = 10000000

    for i in range(len(a)):
        if a[i] < minv:
            minv = a[i]
            mini = i
    return mini

for i in range(n):
    c.append(sum(map(int, input().split())))

for i in range(n):
    next_c = find_min(c)
    c[next_c] = 100000001
    print(next_c+1, end=" ")
