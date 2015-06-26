#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

for j in range(int(input())):

    n = int(input())
    a = list(map(int, input().split()))

    full = sum(a)

    s = 0
    l = 0
    r = 0

    # Could be wrapped in function for shortness
    yes = False

    for i in range(n):

        if i == 0:
            l = 0
        else:
            l = s
                
        if i == n - 1:
            r = 0
        else:
            r = full - s - a[i]

        if l == r:
            yes = True

        s += a[i]

    if yes:
        print("YES")
    else:
        print("NO")


