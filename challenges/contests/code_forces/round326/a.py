#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())

a = []
p = []

for i in range(n):
    inp = input().split()

    a.append(int(inp[0]))
    p.append(int(inp[1]))
    
answ = 0
price = 101

for i in range(n):
    price = min(price, p[i])
    answ += price * a[i]

print(answ)

