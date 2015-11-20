#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a1 = []
b1 = []

for i in range(len(a)):
    a1.append([a[i], i])
for i in range(len(b)):
    b1.append([b[i], i])

a1.sort(key=lambda x: x[0])
b1.sort(key=lambda x: x[0])


def answer(a1, b1):
    i = 0
    j = 0 
    r = []
    for l in range(len(b1)):
        r.append(0)

    la1 = len(a1)
    lb1 = len(b1)
     
    c = "Possible"
    for l in range(1, len(a1)):
        if a1[l][0] == a1[l-1][0]:
            c = "Ambiguity"

    while i < la1 and j < lb1:
        while i < la1 and a1[i][0] != b1[j][0]:
            i += 1
        if i == la1:
            c = "Impossible"
            return (c, [])
        r[b1[j][1]] = a1[i][1]
        j += 1
    return (c, r)    

l, k = answer(a1, b1)

if l == "Possible":
    print(l)
    for e in k:
        print(e+1, end=' ')
    print()
else:
    print(l)
