#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())

a = [int(i) for i in input().split()]

i = 0
answ = n
c = 0

while i < n and a[i] == 0:
    i += 1
    answ -= 1

if i == n:
    print(0)
    exit()

while i < n:
    if a[i] == 0:
        c += 1
    else:
        if c > 1:
            answ -= c
        c = 0
    i += 1
    
answ -= c

print(answ)
