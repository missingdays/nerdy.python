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

l = []

while n > 0:
    i = 0
    while pow(2, i) <= n:
        i += 1

    l.append(i)
    n -= pow(2, i-1)

for e in l:
    print(e, end=" ")
print()
