#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

for i in range(int(input())):

    a = input()

    prices = list(map(int, raw_input().split()))
    profit = 0
    for elem in prices:
        profit -= elem

    end_point = len(prices)-1
    start_point = end_point

    v = prices[end_point]


    while end_point > -1:
        start_point -= 1
        while prices[end_point]>prices[start_point] and start_point > -1:
            start_point -= 1
        s = prices[start_point+1:end_point+1]
        diff = (len(s)) * prices[end_point]
        profit += diff
        end_point = start_point
    print(profit)
