#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def find_min(a):
    m = a[0]
    for elem in a:
        if elem < m:
            m = elem
    return m        

n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))

c1 = [0 for i in range(200)]
c2 = [0 for i in range(200)]

de = find_min(a2)

for elem in a1:
    c1[elem-de] += 1
for elem in a2:
    c2[elem-de] += 1

for i in range(200):
    c2[i] -= c1[i]

for i in range(200):
    if c2[i] > 0:
        print(i+de, end=" ")


