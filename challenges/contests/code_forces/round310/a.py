#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())
s = input()

o = z = 0

for c in s:
    if c == "1":
        o += 1
    else:
        z += 1
print(abs(o-z))        
