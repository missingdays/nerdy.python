#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from math import ceil

def dev(a, c):
    return ceil(a / c)

a, b, c = list(map(int, input().split()))

a = dev(a, c)
b = dev(b, c)

result = a * b

if result == 0:
    result = 1

print(result)
