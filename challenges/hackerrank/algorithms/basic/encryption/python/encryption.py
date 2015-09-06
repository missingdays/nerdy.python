#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from math import sqrt, ceil

s = input()

step = ceil(sqrt(len(s)))

final = []
i = 0

while i < ceil(len(s)/step)+1 and i < step:
    h = []
    j = i

    while j < len(s):
        h.append(s[j])
        j += step

    final.append("".join(h))
    i += 1

print(" ".join(final))    
