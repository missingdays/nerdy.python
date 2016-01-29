#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def shift(a, n):

    b = [["." for i in range(n)] for i in range(3)]

    for i in range(3):
        for j in range(n-2):
            b[i][j] = a[i][j+2]

    return b

n = int(input())

for case in range(n):
    n, k = [int(i) for i in input().split()]

    a = []

    for i in range(3):
        a.append(list(input()))

    m = [[False for i in range(n)] for j in range(3)]


    for i in range(3):
        if a[i][0] == 's':
            m[i][0] = True

    for i in range(1, n):
        #print(a)
        for j in range(3):
            if m[j][i-1] and a[j][i] == "." and (a[j][i-1] == "." or a[j][i-1] == "s") and (i < 2 or a[j][i-2] == "."):
                m[j][i] = True

        ms = [False for something in range(3)]

        if m[0][i]:
            if a[1][i] == ".":
                ms[1] = True
        if m[1][i]:
            if a[0][i] == ".":
                ms[0] = True
            if a[2][i] == ".":
                ms[2] = True
        if m[2][i]:
            if a[1][i] == ".":
                ms[1] = True

        for j in range(3):
            if ms[j]:
                m[j][i] = True

        a = shift(a, n)

    for i in range(3):
        if m[i][n-1]:
            print("YES")
            break
    else:
        print("NO")
    
