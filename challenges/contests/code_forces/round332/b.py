#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def calc(f, b):
    a = [0 for i in range(1000001)]
    ambiguity = False
    for i in range(len(f)):
        e = f[i]
        if a[e] == 0:
            a[e] = i+1
        else:
            a[e] = -1

    r = []

    for e in b:
        if a[e] == 0:
            return "Impossible"
        elif a[e] == -1:
            ambiguity = True
        r.append(a[e])

    if ambiguity:
        return "Ambiguity"
    return "Possible\n" + str.join(' ', list(str(e) for e in r))
    

n, m = list(map(int, input().split()))

f = list(map(int, input().split()))
b = list(map(int, input().split()))


print(calc(f, b))
