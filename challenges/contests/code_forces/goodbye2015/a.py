#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

t = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s = input().split()

n = int(s[0])

answ = 0
if s[2] == "week":
    cur = 5

    for i in range(366):
        if n == cur:
            answ += 1
        cur += 1
        if cur > 7:
            cur= 1
else:
    for i in range(12):
        if n <= t[i]:
            answ += 1

print(answ)
