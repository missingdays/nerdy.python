#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

m = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

def get_segments(a):
    global m

    s = 0

    while a > 0:
        n = a % 10
        s += m[n]
        a //= 10

    return s

a, b = [int(i) for i in input().split()]

s = 0

for i in range(a, b+1):
    s += get_segments(i)

print(s)
