#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

x = abs(x2 - x1)
y = abs(y2 - y1)

print(max(x, y))
