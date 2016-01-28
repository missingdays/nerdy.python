#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

b = []

for i in range(min(k, len(a))):
    b.append(a.pop())
for i in range(min(n - k, len(a))):
    b[k-i-1] += a.pop()

print(max(b))
