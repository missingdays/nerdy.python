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



n = int(input())
a = read_list()

pos = new_list(n)

for i in range(n):
    pos[a[i]-1] = i

s = 0

for i in range(1, n):
    s += abs(pos[i]-pos[i-1])

print(s)
