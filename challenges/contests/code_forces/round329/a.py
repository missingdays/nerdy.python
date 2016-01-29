#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from string import ascii_lowercase

n = int(input())

cs = {}

for c in ascii_lowercase:
    cs[c] = 0

for i in range(n):
    s = input()

    _cs = {}

    for c in s:
        if c in _cs:
            _cs[c] += 1
        else:
            _cs[c] = 1

    k = list(_cs.keys())

    if len(k) == 1:
        cs[k[0]] += _cs[k[0]]
    elif len(k) == 2:
        ns = "".join(sorted(k))

        if ns not in cs:
            cs[ns] = 0

        cs[ns] += _cs[k[0]]
        cs[ns] += _cs[k[1]]

m = 0 

for c0 in ascii_lowercase:
    for c1 in ascii_lowercase:
        if c0 == c1:
            continue

        current = 0

        current += cs[c0]
        current += cs[c1]

        ns = "".join(sorted(c0+c1))

        if ns in cs:
            current += cs[ns]

        m = max(m, current)

print(m)
