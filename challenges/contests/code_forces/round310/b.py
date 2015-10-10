#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def rotate(a, n):
    clock = True
    for i in range(n):
        if clock:
            if a[i] == n-1:
                a[i] = 0
            else:
                a[i] += 1
        else:
            if a[i] == 0:
                a[i] = n-1
            else:
                a[i] -= 1
        clock = not clock
    return a    

def check(a):
    for i in range(len(a)):
        if a[i] != i:
            return False
    return True    

n = int(input())
a = list(map(int, input().split()))

while a[0] != 0:
    a = rotate(a, n)

yes = check(a)

if yes:
    print("YES")
else:
    print("NO")
