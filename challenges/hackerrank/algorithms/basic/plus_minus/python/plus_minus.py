#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())
a = list(map(int, input().split()))

zeros = 0
pluses = 0
minuses = 0

for elem in a:
    if elem == 0:
        zeros += 1
    elif elem > 0:
        pluses += 1
    else:
        minuses += 1

print(pluses / n)
print(minuses / n)
print(zeros / n)
