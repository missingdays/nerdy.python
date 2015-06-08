#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Python sets challenge solution
"""
a = set()
b = set()

# Consume size
input()
inp = input().split()

for elem in list(map(int, inp)): 
    a.add(elem)

# Consume size
input()
inp = input().split()

for elem in list(map(int, inp)):
    b.add(elem)

answ = []

for elem in a.difference(b):
    answ.append(elem)
for elem in b.difference(a):
    answ.append(elem)

answ.sort()

for elem in answ:
    print elem

