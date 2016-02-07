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

n, k = read_list()

a = new_matrix(n, n)

cmi = 1
cma = n**2

for i in range(n):

    for j in range(k-1):
        a[i][j] = cmi
        cmi += 1
    for j in range(n-1, k-2, -1):
        a[i][j] = cma
        cma -= 1
s = 0
for i in range(n):
    s += a[i][k-1]

print(s)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
    
