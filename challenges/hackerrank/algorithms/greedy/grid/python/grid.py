#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

from string import ascii_lowercase

def index(c):
    return ascii_lowercase.index(c)

for i in range(int(input())):
        n = int(input())
        g = []
        for i in range(n):
            g.append(list(input()))

        for i in range(n):
            g[i].sort()
        yes = True

        for i in range(1, n):
            for j in range(n):
                if index(g[i][j]) < index(g[i-1][j]):
                    yes = False
        if yes:
            print("YES")
        else:
            print("NO")
