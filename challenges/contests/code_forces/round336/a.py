#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def find_biggest(n, ps, s):
    n -= 1
    i = 0
    m = 0

    while n >= 0 and ps[n][0] == s:
        i = n
        m = max(m, ps[n][1])
        n -= 1

    return m, i    

def calc(n, ps, s, time):
    if n == 0:
        return s

    if s == 0:
        return 0

    if ps[n-1][0] == s:
        biggest, i = find_biggest(n, ps, s)

        if time >= biggest:
            return 1 + calc(i, ps[:i], s-1, time+1)

        return biggest + calc(i, ps[:i], s-1, biggest+1) - time + 1
    else:
        return s - ps[n-1][0] + calc(n, ps, ps[n-1][0], time + s - ps[n-1][0]) 



def input_int_array():
    return [int(i) for i in input().split()]

n, s = input_int_array()

ps = []

for i in range(n):
    ps.append(input_int_array())

ps.sort(key=lambda a: a[0])    

print(calc(n, ps, s, 0))
