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


a, b = read_list()

answ = 0

i = 0

while (1 << i) / 2 <= b:
    j = 0
    while j < i-1:
        if a <= (1 << i) - 1 - (1 << j) <= b:
            answ += 1
        j += 1
    i += 1

print(answ)
