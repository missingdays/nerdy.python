#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

inp = input().split()

n = int(inp[0])
k = int(inp[1])

prices = list(map(int, input().split()))

prices.sort()

c = 0

while len(prices) > 0 and prices[0] < k:
    k -= prices.pop(0)
    c += 1
print(c)    


