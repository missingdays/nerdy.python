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

a = [None for i in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

s = 0
for i in range(n):
    s += a[i][i]

for i in range(n):
    s -= a[i][n-i-1]

print(abs(s))    
