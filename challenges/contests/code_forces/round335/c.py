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

a = [int(i) for i in input().split()]

pos = [0 for i in range(n)]

for i in range(len(a)):
    pos[a[i]-1] = i

m = 1
c = 1

for i in range(1, len(pos)):
    if pos[i] >= pos[i-1]:
        c += 1
    else:
        m = max(m, c)
        c = 1

m = max(m, c)

print(n-m)
