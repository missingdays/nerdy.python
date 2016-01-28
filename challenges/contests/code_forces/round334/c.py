#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())
s = input()

res = 1

for i in range(1, n):
    if s[i] != s[i-1]:
        res += 1

print(min(res+2, n))
