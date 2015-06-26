#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from string import ascii_lowercase, ascii_uppercase

input()
s = input()
k = int(input())

enc = []

for c in s:
    if c in ascii_lowercase:
        enc.append(ascii_lowercase[(ascii_lowercase.index(c)+k) % 26])
    elif c in ascii_uppercase:
        enc.append(ascii_uppercase[(ascii_uppercase.index(c)+k) % 26])
    else:
        enc.append(c)
print(''.join(enc))        

