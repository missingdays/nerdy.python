#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Gem stones challenge solution
"""

import string

def check(strings, c):
    yes = True
    for string in strings:
        if not c in string:
            yes = False
    return yes

n = int(input())

strings = []

for i in range(n):
    strings.append(input())

letters = [0 for i in range(26)]

for i in range(26):
    if check(strings, string.ascii_letters[i]):
        letters[i] = 1

print(sum(letters))        

