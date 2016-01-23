#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def calc(x1, y1, x2, y2, x3, y3):
    if x1 == x2 == x3 or y1 == y2 == y3:
        return 1

    if x2 == x3 or y2 == y3:
        x1, x3 = x3, x1
        y1, y3 = y3, y1
    if x1 == x3 or y1 == y3:
        x2, x3 = x3, x2
        y2, y3 = y3, y2

    if x1 == x2:
        if y1 < y3 < y2 or y2 < y3 < y1:
            return 3
        else:
            return 2

    if y1 == y2:
        if x1 < x3 < x2 or x2 < x3 < x1:
            return 3
        else:
            return 2

    return 3    

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]
x3, y3 = [int(i) for i in input().split()]

print(calc(x1, y1, x2, y2, x3, y3))
