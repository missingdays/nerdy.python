#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

ps = [500, 1000, 1500, 2000, 2500]

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

c = [int(i) for i in input().split()]

pts = 0

for i in range(5):
    pts += max(0.3*ps[i], (1-a[i]/250)*ps[i] - 50*b[i])

pts += c[0] * 100;
pts -= c[1] * 50;

print(int(pts))
