#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from string import ascii_lowercase
l = ascii_lowercase

[n, m] = list(map(int, input().split()))
s = input()

a = [None] * n

for i in range(n):
    a[i] = l.index(s[i])

alpha = [i for i in range(26)]

for i in range(m):
    al, bl = input().split()

    ai = l.index(al)
    bi = l.index(bl)

    ai = alpha.index(ai)
    bi = alpha.index(bi)

    alpha[ai], alpha[bi] = alpha[bi], alpha[ai]


for i in range(n):
    print(l[alpha[a[i]]], end="")
print()
