#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

input()

def buy(a):
    k = a[0]
    while len(a) > 0 and a[0] <= k+4:
        a.pop(0)
    return a

a = list(map(int, input().split()))
a.sort()

c = 0

while len(a) > 0:
    a = buy(a)
    c += 1
print(c)    

