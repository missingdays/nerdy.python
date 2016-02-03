#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def isCorrectNumber(n):
    if len(n) == 0:
        return False

    if len(n) == 1:
        return "0" <= n[0] <= "9"

    if not ("0" < n[0] <= "9"):
        return False

    for i in range(1, len(n)):
        if not ("0" <= n[i] <= "9"):
            return False
    return True

# append terminator
s = input() + ";"

a, b = [], []

ss = ""

for c in s:
    if c == ";" or c == ",":
        if isCorrectNumber(ss):
            a.append(ss)
        else:
            b.append(ss)

        ss = ""
    else:
        ss += c

if len(a) == 0:
    print("-")
else:
    print('"', end="")
    print(",".join(a), end="")
    print('"')
if len(b) == 0:
    print("-")
else:
    print('"', end="")
    print(",".join(b), end="")
    print('"')
