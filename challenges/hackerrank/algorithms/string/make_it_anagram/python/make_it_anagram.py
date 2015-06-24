#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Make in anagram challenge solution
"""

from string import ascii_letters

s1 = input()
s2 = input()

sl1 = [0 for i in range(26)]
sl2 = [0 for i in range(26)]

for c in s1:
    sl1[ascii_letters.index(c)] += 1
for c in s2:
    sl2[ascii_letters.index(c)] += 1

dels = 0

for i in range(26):
    dels += abs(sl1[i]-sl2[i])

print(dels)    
