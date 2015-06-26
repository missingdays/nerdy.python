#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def check(m, n, a):
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == m:
                return i, j

for case in range(int(input())):

    m = int(input())
    n = int(input())
    a = list(map(int, input().split()))

    i, j = check(m, n, a)
    print(i+1, j+1)
