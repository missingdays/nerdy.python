#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

import math

n = int(input())

i = 2

while i < int(pow(n, 1/2)) + 1:
    yep = False
    while n % i == 0:
        n //= i
        yep = True

    if yep:
        n *= i

    i += 1

print(n)
