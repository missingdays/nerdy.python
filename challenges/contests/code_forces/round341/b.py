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


n = int(input())

a = new_matrix(1000, 1000)

for i in range(n):
    bishop = read_list()

    a[bishop[0]-1][bishop[1]-1] = 1

answ = 0

for i in range(1000):
    c = 0

    l = i
    r = 0

    while l < 1000:
        c += a[l][r]
        l += 1
        r += 1

    answ += c*(c-1)

for i in range(1, 1000):
    c = 0

    l = 0
    r = i

    while r < 1000:
        c += a[l][r]
        l += 1
        r += 1

    answ += c*(c-1)

for i in range(1000):
    c = 0

    l = 999
    r = i

    while r < 1000:
        c += a[l][r]
        l -= 1
        r += 1

    answ += c*(c-1)

for i in range(1, 1000):
    c = 0

    l = 999-i
    r = 0

    while l > -1:
        c += a[l][r]
        l -= 1
        r += 1

    answ += c*(c-1)

print(answ//2)
