#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

import sys

n = int(input())
a = [int(i) for i in input().split()]

if not 1 in a:
    print(0)
    sys.exit()

i = 0
while i < n and a[i] == 0:
    i += 1

j = n - 1
while j >= 0 and a[j] == 0:
    j -= 1

overall = 1
current = 1
while i < j:
    while i < j and a[i] == 0:
        current += 1
        i += 1

    overall *= current    

    while i < j and a[i] == 1:
        i += 1

    current = 1    

print(overall)
