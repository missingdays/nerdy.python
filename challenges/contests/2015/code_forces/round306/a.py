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

yes = False

if "AB" in s:
    i = s.index("AB")

    n = s[:i] + " " + s[i+2:]

    if n.count("BA") > 0:
        yes = True
if "BA" in s:
    i = s.index("BA")

    n = s[:i] + " " + s[i+2:]

    if n.count("AB") > 0:
        yes = True
if yes:
    print("YES")
else:
    print("NO")




