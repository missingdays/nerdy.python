#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

import string

uppercase = string.ascii_uppercase

def is_rc(s):
    if s[0] != "R":
        return False
    if not s[1].isnumeric():
        return False
    i = 1
    while i < len(s) and s[i].isnumeric():
        i+=1
    if i == len(s) or s[i] != "C":
        return False
    return s[i+1].isnumeric()

def convert_rc(s):
    v = int(s) 
    l = len(uppercase)
    o = []
    while v > 0:
        v -= 1
        o.insert(0, uppercase[(v % l)])
        v //= l
    return "".join(o)

def from_rc(s):
    i = 1

    row = []
    while s[i] != "C":
        row.append(s[i])
        i+=1
    rows = "".join(row)

    i+=1
    col = []
    while i < len(s):
        col.append(s[i])
        i+=1
    cols = "".join(col)
    cols = convert_rc(cols)

    return cols + rows

def convert_excel(s):
    l = len(uppercase)
    i = len(s) - 1
    v = 0
    while i >= 0:
        v += ((uppercase.index(s[i])+1) * pow(l, (len(s) - i - 1)))
        i -= 1
    return v    

def from_excel(s):
    row = []
    col = []

    i = 0

    while s[i] in uppercase:
        col.append(s[i])
        i += 1

    cols = str(convert_excel("".join(col)))

    while i < len(s):
        row.append(s[i])
        i += 1

    rows = "".join(row)

    return "R" + rows + "C" + cols

def transform(s):
    if is_rc(s):
        return from_rc(s)
    return from_excel(s)

for i in range(int(input())):
    print(transform(input()))
