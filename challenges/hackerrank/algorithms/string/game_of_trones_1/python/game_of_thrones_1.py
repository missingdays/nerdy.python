#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

import string

s = input()

letters = [0 for i in range(26)]

for c in s:
    letters[string.ascii_letters.index(c)] += 1

yes = True
hadOdd = False

for letter in letters:
    if letter % 2 == 1:
        if hadOdd:
            yes = False
        else:
            hadOdd = True


if yes:
    print("YES")
else:
    print("NO")
