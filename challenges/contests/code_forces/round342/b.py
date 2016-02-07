#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""


s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)

answ = 0
i, j = 0, 0
while i < n1-n2+1:
    j = 0

    subs = True
    while j < n2:
        if s2[j] != s1[i+j]:
            subs = False
            break
        j += 1

    if subs:
        answ += 1
        i += n2
    else:
        i += 1

print(answ)
