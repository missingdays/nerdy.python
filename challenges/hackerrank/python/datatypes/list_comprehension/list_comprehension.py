#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Python list comprehension challenge solution
"""

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

arr = []

for i in range(X+1):
    for j in range(Y+1):
        for k in range(Z+1):
            if i + j + k != N:
                arr.append([i, j, k])

print(arr)
