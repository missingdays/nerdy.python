#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Funny string challenge solution
"""

import string
def index(c):
    return string.ascii_letters.index(c)
for i in range(int(input())):
    s = input()
    sr = s[::-1]

    funny = True

    for i in range(1, len(s)):
        if abs(index(s[i])-index(s[i-1])) != abs(index(sr[i]) - index(sr[i-1])):
            funny = False

    if funny:
        print("Funny")
    else:
        print("Not Funny")


