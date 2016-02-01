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

def calc(a, b):
    return (1 - (1-a)*(1-b))*2000

def in_interval(a, b, p):
    return b//p - (a-1)//p

n, p = read_list()

sh = []
answ = 0

for i in range(n):
    l, r = read_list()

    c = in_interval(l, r, p)

    sh.append(c / (r-l+1))

for i in range(1, n):
    answ += calc(sh[i], sh[i-1])
answ += calc(sh[0], sh[n-1])

print(answ)
