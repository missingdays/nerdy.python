#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def check(c):
    for char in c:
        if char == '0':
            return False
    return True    

n = int(input())

s = []
eq = [0 for i in range(n)]
for i in range(n):
    s.append(input())

clean = 0

for c in s:
    if check(c):
        clean += 1

for i in range(n):
    for j in range(i, n):
        if s[i] == s[j]:
            eq[i] += 1

print(max(clean, max(eq)))            
