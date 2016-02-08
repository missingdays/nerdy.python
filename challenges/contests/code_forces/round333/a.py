#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""
n, b = list(map(int, input().split()))
l1 = list(reversed(list(map(int, input().split()))))

m, a = list(map(int, input().split()))
l2 = list(reversed(list(map(int, input().split()))))

x = 0
y = 0

for i in range(len(l1)):
    x += (l1[i]*pow(b, i))
for i in range(len(l2)):
    y += (l2[i]*pow(a, i))

if x < y:
    print("<")
elif x == y:
    print("=")
else:
    print(">")
