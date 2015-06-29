#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from itertools import combinations

def check(s):
    for i, j, k in combinations(s, 3):
        if int(i + j + k) % 8 == 0:
            return int(i + j + k)
    for i, j in combinations(s,2):    
        if int(i + j) % 8 == 0:
            return int(i + j)
    return -1        

s = input()
if "0" in s:
    print("YES")
    print(0)
elif "8" in s:
    print("YES")
    print(8)
else:
    answ = check(s)
    if answ >= 0:
        print("YES")
        print(answ)
    else:
        print("NO")
