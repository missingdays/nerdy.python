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

a = []
m = []

for i in range(n):
    a.append([int(i) for i in input().split()])

a.sort(key=lambda s: s[0])

l = 0

for b in a:
    l = max(l, b[0])

j = 0

for i in range(l + 1):
    if a[j][0] == i:
        # Destroys all left
        if a[j][1] >= i:
            m.append(1)
        else:
            m.append(m[i-a[j][1]-1] + 1)

        j += 1    
    else:
        if i > 0:
            m.append(m[i-1])
        else:
            m.append(0)

print(n - max(m))
