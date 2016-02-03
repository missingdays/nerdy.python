#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Python solution is not percise enough. Check out the cpp one
"""

from math import sin, cos, pi, sqrt, acos
from decimal import *

def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]
def new_matrix(n, m=0):
    return [[0 for i in range(m)] for i in range(n)]

def s(r1, r2, d):
    al = Decimal(acos(Decimal(r2**2 + d - r1**2) / Decimal(2*r2*Decimal(sqrt(d)))))

    return int(r2**2)*(al - Decimal(sin(al))*Decimal(cos(al)))

x1, y1, r1 = read_list()
x2, y2, r2 = read_list()

d = int(pow(x2-x1, 2) + pow(y2-y1, 2))

if d >= pow(r1 + r2, 2):
    print(0)
    exit()

if d <= pow(r2-r1, 2):
    print(pi*min(r1, r2)**2)
    exit()

print(s(r1, r2, d) + s(r2, r1, d))

