#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

act = list(map(int, input().split()))
req = list(map(int, input().split()))

def compare(act, req, n):
    if act[n] > req[n]:
        return n + 1
    if act[n] < req[n]:
        return -n - 1
    if n == 0:
        return 0
    return compare(act, req, n - 1)

c = compare(act, req, 2)

if c < 0 or c == 0:
    print(0)
else:
    if c == 1:
        print((act[0]-req[0])*15)
    elif c == 2:
        print((act[1]-req[1])*500)
    else:
        print(10000)
