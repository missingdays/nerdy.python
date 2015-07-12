#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""
import pprint

def getRow(row):
    m = 0
    cur = 0
    for v in row:
        if v == 1:
            cur += 1
            if cur > m:
                m = cur
        else:
            cur = 0
    return m       
n, m, k = list(map(int, input().split()))
a = []
v = [0 for i in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    v[i] = getRow(tmp)
    a.append(tmp)
for test in range(k):
   i, j = list(map(int, input().split()))
   i -= 1 # zero-indexed
   j -= 1

   if a[i][j] == 0:
       a[i][j] = 1
   else:
       a[i][j] = 0
   v[i] = getRow(a[i])
   print(max(v))
