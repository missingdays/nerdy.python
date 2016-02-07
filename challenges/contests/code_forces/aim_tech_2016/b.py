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


def dump(a, i):
    while i > 0 and a[i] <= a[i-1]:
        a[i-1] -= 1
        i -= 1

    return a


n = int(input())

a = read_list()

a.sort()

for i in range(1, n):
    a = dump(a, i)

print(sum([i for i in a if i > 0]))
