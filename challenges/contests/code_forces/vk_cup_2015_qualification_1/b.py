#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

class Person():
    def __init__(self, w, h):
        self.h = h
        self.w = w
       

n = int(input())

p = []

for i in range(n):
    w, h = list(map(int, input().split()))

    p.append(Person(w, h))

s = 0
m1 = m2 = 0

for i in p:
    s += i.w

    if i.h > m1:
        m2 = m1
        m1 = i.h
    elif i.h > m2:
        m2 = i.h

for i in range(len(p)):
    h = m1
    if p[i].h == m1:
        h = m2
    print(h * (s-p[i].w), end=" ")
