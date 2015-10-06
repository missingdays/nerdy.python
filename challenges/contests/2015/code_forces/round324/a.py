#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

inp = list(map(int, input().split()))
a = inp[0]
b = inp[1]

c = pow(10, a-1)
c = c // b
c = (c+1) * (b)

if(pow(10, a-1) <= c < pow(10, a)):
    print(c)
else:
    print(-1)

