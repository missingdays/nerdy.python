#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from itertools import combinations

def combos(lst):
    for i in range(0, len(lst)):
        for combo in combinations(lst, i+1):
            yield combo

inp = list(map(int, input().split()))
n = inp[0]
l = inp[1]
r = inp[2]
k = inp[3]

probs = sorted(list(map(int, input().split())))

count = 0

for sublist in combos(probs):
    if (sublist[len(sublist)-1] - sublist[0]) >= k:
        s = sum(sublist)
        if s >= l and s <= r:
            count += 1

print(count)            
