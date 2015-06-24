#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from string import ascii_letters

for i in range(int(input())):
    s1 = input()
    s2 = input()

    sl1 = [0 for i in range(26)]
    sl2 = [0 for i in range(26)]

    for c in s1:
        sl1[ascii_letters.index(c)] += 1
    for c in s2:
        sl2[ascii_letters.index(c)] += 1

    yes = False

    for i in range(26):
        if sl1[i] != 0 and sl2[i] != 0:
            yes = True
    if yes:
        print("YES")
    else:
        print("NO")
        
