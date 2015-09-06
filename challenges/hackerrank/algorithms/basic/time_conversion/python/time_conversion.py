#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

s = input()

if s[-2:] == "AM":
    print(s[:-2])
else:
    a = s.split(":")

    a[0] = str(int(a[0])+12)

    if a[0] == "24":
        a[0] = "00"
    s = ":".join(a)
    print(s[:-2])
