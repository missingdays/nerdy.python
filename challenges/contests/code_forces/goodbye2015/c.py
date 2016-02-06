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


m = 2005

h, w = read_list()

d = []
for i in range(h):
    d.append(input())

ver = new_matrix(m, m)
hor = new_matrix(m, m)

for j in range(h):
    for i in range(w):
        hor[i+1][j+1] = hor[i+1][j] + hor[i][j+1] - hor[i][j]
        ver[i+1][j+1] = ver[i+1][j] + ver[i][j+1] - ver[i][j]

        if d[j][i] == ".":
            if i < w-1 and d[j][i+1] == ".":
                hor[i+1][j+1] += 1
            if j < h-1 and d[j+1][i] == ".":
                ver[i+1][j+1] += 1


n = int(input())

for i in range(n):
    y1, x1, y2, x2 = read_list()

    x1 -= 1
    y1 -= 1

    answ = 0
    answ += (hor[x2-1][y2] - hor[x1][y2] - hor[x2-1][y1] + hor[x1][y1])
    answ += (ver[x2][y2-1] - ver[x1][y2-1] - ver[x2][y1] + ver[x1][y1])

    print(answ)
