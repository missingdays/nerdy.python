#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def check(a):
    s = 0
    for i in range(1, len(a)):
        if a[i]-1 == a[i-1]:
            s += 1
        else:    
            return s*2
    return s*2    

inp = list(map(int, input().split()))

n, k = inp[0], inp[1]

s = 0

for line in range(k):
    inp = list(map(int, input().split()))
    if inp[1] == 1:
        s -= check(inp[1:])
    s += (inp[0] - 1)

s += (n-1)
print(s)


