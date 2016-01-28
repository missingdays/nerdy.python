#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def compute(n, jars):
    m = min(jars)

    l = 0
    ml = 0

    # This is kinda hack so the biggest path 
    # between two minimum jars in 10 10 1 10 is still 3
    
    for i in range(n):
        if jars[i] == m:
            if l > ml:
                ml = l 
            l = 0
        else:
            l += 1

    for i in range(n):
        if jars[i] == m:
            if l > ml:
                ml = l 
            l = 0
        else:
            l += 1

    return n*m + ml

n = int(input())

jars = list(map(int, input().split()))

print(compute(n, jars))

