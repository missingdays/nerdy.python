#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

a = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

d = []

for i in range(3):
    if x[i] < a[i]:
        d.append((a[i]-x[i])//2)
    else:
        d.append(a[i]-x[i])

if sum(d) >= 0:
    print("YES")
else:
    print("NO")
