#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Sherlock and the beast solution
"""

for i in range(int(input())):
    N = int(input())

    S = ""

    while N % 3 != 0 and N > 0:
        S = S + "3"*5
        N -= 5
    if N % 3 != 0:
        print(-1)
    else:
        while N > 0:
            S = "5"*3 + S
            N -= 3
        print(S)
