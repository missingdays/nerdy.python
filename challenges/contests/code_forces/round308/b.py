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
count = 9 
s = 0

while n > 0:
    if n > count:
        s += count*len(str(count)) 
    else:
        s += n * len(str(count))
    n -= count 
    count *= 10
print(s)
