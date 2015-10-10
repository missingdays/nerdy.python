#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""
s = 0
for i in range(int(input())):
    l = list(map(int, input().split()))
    sq = (l[2]-l[0]+1)*(l[3]-l[1]+1)
    s += sq
print(s)
