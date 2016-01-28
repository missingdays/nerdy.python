#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

MAXN = int(1e6) + 100

n = int(input())
m = [0 for i in range(MAXN)]
answ = 0

a = list(map(int, input().split()))

for e in a:
    m[e] += 1

for i in range(MAXN-1):
    m[i+1] += m[i]//2

    m[i] %= 2

    answ += m[i]

print(answ)
