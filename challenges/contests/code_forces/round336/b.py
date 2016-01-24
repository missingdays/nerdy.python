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

zeros = 0
ones = 0

i = 0
j = -1 

l1 = len(s1)
l2 = len(s2)

answ = 0

while j < l2 - l1:
    j += 1
    if s2[j] == "0":
        zeros += 1
    else:
        ones += 1

while j < l2:
    if s1[i] == "0":
        answ += ones
    else:
        answ += zeros

    if j == l2 - 1:
        break

    j += 1
    i += 1

    if s2[i-1] == "0" and s2[j] == "1":
        zeros -= 1
        ones += 1
    elif s2[i-1] == "1" and s2[j] == "0":
        zeros += 1
        ones -= 1


print(answ)        
