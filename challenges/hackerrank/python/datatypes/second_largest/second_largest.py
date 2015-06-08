#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Python second largest challenge solution
"""

# Consume the size

input()

arr = list(map(int, input().split()))

# a is the largest number
# b is the second largest number
a, b = -101, - 101

for elem in arr:
    if elem > a and elem != b:
        a, b = elem, a
    elif elem > b and elem != a:
        b = elem
print(b)
