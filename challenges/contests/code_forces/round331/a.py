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

def calc(a, n):
    for i in range(n):
        for j in range(i, n):
            if a[i][0] != a[j][0] and a[i][1] != a[j][1]:
                return abs(a[i][0] - a[j][0])*abs(a[i][1] - a[j][1])
    return -1

if n == 1:
    print(-1)
else:
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    print(calc(a, n))    
          
