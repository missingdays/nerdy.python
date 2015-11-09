#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

a = int(input())

ns = []

# sum(ns)
s = 0

for i in range(1, a+1):
    if s == a:
        break

    if i < (a-s)/2 or s + i == a:
        s += i
        ns.append(i)

print(len(ns))

for e in ns:
    print(e, end=' ')
print()    
