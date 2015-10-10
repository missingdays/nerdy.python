#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def convert(base, n):
    l = [0 for i in range(100)]
    c = 99 
    while n > 0:
        a = n // base
        b = n % base
        l[c] = b
        c -= 1
        n = a
    return l

def arr_eq(a, b):
    for i in range(99, 0, -1):
        if a[i]!=b[i]:
            return False
    return True

def inc_arr(arr, ptr, base):
    arr[ptr] = 0
    while ptr > 0:
        if arr[ptr-1] == base - 1:
            arr[ptr-1] = 0 
        else:
            arr[ptr-1] += 1
            return arr
        ptr-=1
    return arr

def weight(sc1, sc2, base):
    ptr = 99
    while not arr_eq(sc1, sc2) and ptr > -1:
        if sc1[ptr] == 1:
            sc2[ptr] = 1
        elif sc1[ptr] == base - 1:
            sc1 = inc_arr(sc1, ptr, base)
        elif sc1[ptr] == 0:
            pass
        else:
            return False
        ptr -= 1
    return arr_eq(sc1, sc2)
inp = input().split()

base = int(inp[0])

n = int(inp[1])

l = convert(base, n)
sc1, sc2 = l, [0 for i in range(100)]

i = weight(sc1, sc2, base)
if i:
    print("YES")
else:
    print("NO")
