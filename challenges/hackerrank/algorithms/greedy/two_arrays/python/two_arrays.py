#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def check(l1, l2, k):
    n = len(l1)
    for i in range(n):
        if l1[i] + l2[i] < k:
            return False
    return True

for i in range(int(input())):
    inp = input().split()
    n = int(inp[0])
    k = int(inp[1])

    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    l1.sort()
    l2.sort(reverse=True)

    yes = check(l1, l2, k)

    if yes:
        print("YES")
    else:
        print("NO")

