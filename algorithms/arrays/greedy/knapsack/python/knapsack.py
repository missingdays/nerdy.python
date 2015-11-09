#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
    type: algorithm
    theme: arrays
    sub-theme: greedy
    name: knapsack problem
    author of code: Evgeny @missingdays Bovykin
"""

n, weight = list(map(int, input().split()))

things = []

for i in range(n):
    things.append(list(map(int, input().split())))

things.sort(key = lambda x: -x[0]/x[1])

money = 0

for thing in things:
    if weight == 0:
        break
    if thing[1] <= weight:
        money += thing[0]
        weight -= thing[1]
    else:
        money += thing[0]/thing[1]*weight
        weight = 0

print(money)        
