#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]
def new_matrix(n, m=0):
    return [[0 for i in range(m)] for i in range(n)]

n, m = read_list()

_a = read_list()
_b = read_list()

a, b = [], []

for i in range(n):
    a.append([_a[i], i])
for i in range(m):
    b.append([_b[i], i])

a.sort(key=lambda u: u[0])
b.sort(key=lambda u: u[0])

answ = new_list(m)

i = j = c = 0

while i < n and  j < m:
    if a[i][0] <= b[j][0]:
        c += 1
        i += 1
    else:
        answ[b[j][1]] = c
        j += 1
while j < m:
    answ[b[j][1]] = c
    j += 1
print(" ".join([str(i) for i in answ]))
