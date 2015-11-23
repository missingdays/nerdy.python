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

a = list(map(int, input().split()))
s = 0
steps = 0

for e in a:
    steps += abs(e-s)
    s = e

print(steps)    
