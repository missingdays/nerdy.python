#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
C4 hard part solution for satelite problem
"""

prev_three= [0,0,0]
cur_max = 0
prev_max = 0

for i in range(int(input())):

    if i < 3:
        prev_three[i] = int(input())

    else:
        inp = int(input())

        if prev_three[i%3] > prev_max:
            prev_max = prev_three[i%3]

        prev_three[i%3] = inp

        if inp > cur_max:
            cur_max = inp

print(prev_max * cur_max)
    
