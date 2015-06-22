#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def get_v(arr, i):
    if i >= 0:
        return arr[i]
    return 0

inp = list(map(int, input().split()))
N = inp[0]
C = inp[1]

coins = list(map(int, input().split()))
coins.sort()

vals = [None for i in range(N+1)]
for i in range(N+1):
    vals[i] = [0 for j in range(C+1)]

for i in range(1, C+1):
    vals[0][i] = 1

for i in range(1, N+1):
    vals[i][0] = 0
    
    for j in range(1, C+1):
        value = vals[i][j-1]

        if coins[j-1] <= i:
            value += vals[i-coins[j-1]][j]

        vals[i][j] = value

print(vals[N][C])
