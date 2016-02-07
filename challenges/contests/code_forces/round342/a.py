#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""
def read_list():
    return [int(i) for i in input().split()]
def new_list(n):
    return [0 for i in range(n)]
def new_matrix(n, m=0):
    return [[0 for i in range(m)] for i in range(n)]


n = int(input())

a = int(input())
b = int(input())
c = int(input())

if a < b-c:
    print(n//a)
elif n < b:
    print(n//a)
else:
    diff = b-c

    answ = (n-b)//diff

    n -= answ*b
    n += answ*c

    if n >= b:
        n -= b
        n += c
        answ += 1
    answ += n//a

    print(max(answ, 0))

