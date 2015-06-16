#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def check(array):
    for elem in array:
        if elem == 1 or elem == 3:
            return False
    return True        

n = int(input())

a = [ [ None for j in range(n) ] for i in range(n)]

for i in range(n):
    inp = list(map(int, input().split()))

    for j in range(len(inp)):
        a[i][j] = inp[j]

good = []

for i in range(n):
    if check(a[i]):
       good.append(i+1)

print(len(good))
for elem in good:
    print(elem, end=" ") 
