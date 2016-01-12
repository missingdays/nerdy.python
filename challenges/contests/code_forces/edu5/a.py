#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def calc(a, b, l):
    for i in range(l):
        if int(a[i]) > int(b[i]):
            return ">"
        elif int(a[i]) < int(b[i]):
            return "<"

    return "="    

a = input()
b = input()

al = len(a)
bl = len(b)

if bl > al:
    a = "0" * (bl - al) + a
    al = bl
elif al > bl:
    b = "0" * (al - bl) + b
    bl = al

print(calc(a, b, bl))
