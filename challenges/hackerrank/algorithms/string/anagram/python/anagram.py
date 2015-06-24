#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""
for i in range(int(input())):
    s = input()

    if len(s) % 2 == 1:
        print(-1)
    else:
        s1 = list(s[:len(s)//2])
        s2 = list(s[len(s)//2:])
        count = 0

        for c in s1:
            if not c in s2:
                count += 1
            else:
                s2.remove(c)
        print(count)

