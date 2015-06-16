#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Number theory restaurant solution
"""

# This version of gcd was faster to code :P
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

for i in range(int(input())):
    inp = list(map(int, input().split()))

    g=gcd(inp[0], inp[1])

    print(int(inp[0]*inp[1]/(g*g)))
