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

a = [i for i in input().split()]

def change(l, r):
    global a

    if l == r:
        return 0

    if a[l] == a[r]:
        for i in range(l+1, r):
            a[i] = a[l]
        return (r-l)//2
    else:
        m = (l+r+1)//2

        for i in range(l+1, m):
            a[i] = a[l]

        for i in range(m, r):
            a[i] = a[r]

        return (r-l-1)//2


answ = 0
current = 0

for i in range(n):
    if i == n-1 or a[i] == a[i+1]:
        answ = max(answ, change(current, i))
        current = i+1

print(answ)
print(" ".join(a))
